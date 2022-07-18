# 飞书机器人webhook


import requests
import json
import logging
from larkbot_table import APITable

logger = logging.getLogger('feishu')


class LarkBot(APITable):
    def __init__(self, app_id, app_secret) -> None:
        self.app_id = app_id
        self.app_secret = app_secret
        self._token = ''

    # def send_webhook(self, content: str, webhook: str) -> None:
    #     resp = requests.request("POST", webhook, headers=self.headers, data=json.dumps(content))
    #     resp.raise_for_status()
    #     result = resp.json()
    #     if result.get("code") and result["code"] != 0:
    #         print(result["msg"])
    #         return

    @property
    def get_token(self):
        if len(self._token) == 0:
            token_url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal'
            payload_message = {
                "app_id": self.app_id,
                "app_secret": self.app_secret
            }
            response = self._post(token_url, payload_message, with_token=False)
            self._token = response.get("tenant_access_token")
            return self._token
        return self._token

    def _base_request(self, method,
                      url,
                      body=None,
                      files=None,
                      with_token=True,
                      success_code=0):
        headers = {}
        if with_token:
            token = self.get_token
            headers['Authorization'] = 'Bearer {}'.format(token)

        if files and body:
            r = requests.request(method=method, data=body, url=url, files=files, headers=headers)
        elif files:
            r = requests.request(method=method, url=url, files=files, headers=headers)
        elif body:
            headers['Content-Type'] = 'application/json'
            r = requests.request(method=method, url=url, json=body, headers=headers)
        else:
            r = requests.request(method=method, url=url, headers=headers)

        try:
            res = r.json()
        except Exception:
            logger.error('[http] method=%s, url=%s, body=%s, files=%s, status_code=%d, res=%s',
                         method, url, body, files, r.status_code, r.text)
            # 为了记录 error 日志，所以原样抛出
            raise

        code = res.get('code')
        if code is not None and isinstance(code, int) and code != success_code:
            # 抛出 OpenLarkException
            raise Exception(r.text)
        error = res.get('error')
        if error is not None and isinstance(error, int) and error != success_code:
            raise Exception(error)

        return res

    def _post(self, url, body=None, files=None, with_token=True, success_code=0):
        return self._base_request('post', url=url,
                                  body=body,
                                  files=files,
                                  with_token=with_token,
                                  success_code=success_code)

    def _get(self, url, with_token=True, success_code=0):
        return self._base_request('get', url=url,
                                  with_token=with_token,
                                  success_code=success_code)

    def _delete(self, url, with_token=True, success_code=0):
        return self._base_request('delete', url=url,
                                  with_token=with_token,
                                  success_code=success_code)

    def _put(self, url, body=None, with_token=True, success_code=0):
        return self._base_request('put', url=url,
                                  body=body,
                                  with_token=with_token,
                                  success_code=success_code)

    def send_chat_file(self, receive_id, filekey):
        url = 'https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type=chat_id'
        body = {
            "receive_id": receive_id,
            "content": "{\"file_key\":\"" + filekey + "\"}",
            "msg_type": "file"
        }
        self._post(url, body=body)

    def get_chat_id(self):
        url = 'https://open.feishu.cn/open-apis/im/v1/chats'
        response = self._get(url)

    def upload_file(self, filename, filepath, filetype='xls'):
        url = 'https://open.feishu.cn/open-apis/im/v1/files'
        body = {
            'file_type': filetype,
            'file_name': filename
        }

        files = {'file': open(filepath, 'rb+')}
        response = self._post(url=url, body=body, files=files)
        return response['data']['file_key']



