class APITable(object):
    def get_drive_root_folder_meta(self, tenent_access_token):
        """获取root folder（我的空间） meta
        :type self: LarkBot
        :param tenent_access_token: tenent_access_token
        :type tenent_access_token: str
        :return: 文件夹ID
        :rtype: str
        该接口用于获取 "我的文档" 的元信息
        https://open.feishu.cn/document/ukTMukTMukTM/ugTNzUjL4UzM14CO1MTN/get-root-folder-meta
        """
        url = 'https://open.feishu.cn/open-apis/drive/explorer/v2/root_folder/meta'
        res = self._get(url, with_token=tenent_access_token)
        return res['data']['token']

    def create_drive_file(self, tenent_access_token, folder_token, title, file_type='bitable'):
        """创建云空间文件
        :type self: OpenLark
        :param user_access_token: tenent_access_token
        :type user_access_token: str
        :param folder_token: 文件夹的 token
        :type folder_token: str
        :param title: 文档标题
        :type title: str
        :param file_type: 文档类型，可选值为 "doc" 、 "sheet" or "bitable"
        :type file_type: DriveFileType
        :return: jsondata
        :rtype: str
        该接口用于根据 folder_token 创建 "doc" 、 "sheet" or "bitable" 。
        https://open.feishu.cn/document/ukTMukTMukTM/uQTNzUjL0UzM14CN1MTN
        """
        url = f'https://open.feishu.cn/open-apis/drive/explorer/v2/file/{folder_token}'
        body = {
            'title': title,
            'type': file_type,
        }
        res = self._post(url, body=body, with_token=tenent_access_token)
        return res['data']

    def get_drive_folder_children(self, tenent_access_token, folder_token):
        """获取文件夹下的文档清单
        :type self: OpenLark
        :param user_access_token: tenent_access_token
        :type user_access_token: str
        :param folder_token: 文件夹的 token
        :type folder_token: str
        :return: 该文件夹的文档清单，如 doc、sheet、bitable、folder
        :rtype: list[DriveFileToken]
        该接口用于获取 "我的文档" 的元信息
        https://open.feishu.cn/document/ukTMukTMukTM/uEjNzUjLxYzM14SM2MTN
        """
        url = f'https://open.feishu.cn/open-apis/drive/explorer/v2/folder/{folder_token}/children'
        res = self._get(url, with_token=tenent_access_token)
        return res['data']['children'].items()

    def add_drive_file_permission(self, tenent_access_token, file_token):
        """增加权限
        :type self: OpenLark
        :param user_access_token: user_access_token
        :type user_access_token: str
        :param file_token: 文件的 token
        :type file_token: str
        :param file_type: 文件类型
        :type file_type: DriveFileType
        :param members: 要添加的权限的人
        :type members: list[DriveFileUserPermission]
        :rtype: list[DriveFileUserPermission]
        该接口用于根据 file_token 给用户增加文档的权限
        https://open.feishu.cn/document/ukTMukTMukTM/uMzNzUjLzczM14yM3MTN
        """
        url = f'https://open.feishu.cn/open-apis/drive/v1/permissions/{file_token}/members?type=bitable'
        body = {
            'member_type': 'openid',
            'member_id': 'ou_7894448b1ad68958ea1dd141d3c5b45e',
            'perm': 'full_access'
        }
        res = self._post(url, body=body, with_token=tenent_access_token)

        return res

    def get_bitable_table_list(self, tenent_access_token, app_token):
        """获取多维表格的table列表
        :type self: OpenLark
        :param tenent_access_token: tenent_access_token
        :type tenent_access_token: str
        :param app_token: 多维表格的 token
        :type app_token: str
        :rtype: list
        该接口用于获取多维表格的table列表
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table/list
        """
        url = f'https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables'
        res = self._get(url, with_token=tenent_access_token)

        return res['data']['items']

    def add_bitable_table(self, tenent_access_token, app_token, table_name):
        """增加多维表格的table
        :type self: OpenLark
        :param tenent_access_token: tenent_access_token
        :type tenent_access_token: str
        :param app_token: 多维表格的 token
        :type app_token: str
        :param table_name: 多维表格的名称
        :type table_name: str
        :rtype: dict
        增加多维表格的table
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table/create
        """
        url = f'https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables'
        body = {
            'table': {
                'name': table_name
            }
        }
        res = self._post(url, body=body, with_token=tenent_access_token)

        return res['data']

    def delete_bitable_table(self, tenent_access_token, app_token, table_id):
        """删除多维表格的table
        :type self: OpenLark
        :param tenent_access_token: tenent_access_token
        :type tenent_access_token: str
        :param app_token: 多维表格的 token
        :type app_token: str
        :param table_id: id
        :type table_id: str
        :rtype: dict
        删除多维表格的table
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table/delete
        """
        url = f'https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}'
        res = self._delete(url, with_token=tenent_access_token)

        return res['data']

    def get_bitable_view_list(self, tenent_access_token, app_token, table_id):
        """获取多维表格的view列表
        :type self: OpenLark
        :param tenent_access_token: tenent_access_token
        :type tenent_access_token: str
        :param app_token: 多维表格的 app_token
        :type app_token: str
        :param table_id: 多维表格的 table_id
        :type table_id: str
        :rtype: list
        该接口用于获取多维表格的view列表
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-view/list
        """
        url = f'https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/views'
        res = self._get(url, with_token=tenent_access_token)

        return res['data']['items']

    def add_bitable_view(self, tenent_access_token, app_token, table_id, view_name, view_type='grid'):
        """增加多维表格的view
        :type self: OpenLark
        :param tenent_access_token: tenent_access_token
        :type tenent_access_token: str
        :param app_token: 多维表格的 token
        :type app_token: str
        :param table_id: 多维表格的 table_id
        :type table_id: str
        :param view_name: 多维表格view的名称
        :type view_name: str
        :param view_type: 多维表格view的类型,grid,kanban,gallery,gantt
        :type view_type: str
        :rtype: dict
        增加多维表格的table
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-view/create
        """
        url = f'https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/views'
        body = {
            'view_name': view_name,
            'view_type': view_type
        }
        res = self._post(url, body=body, with_token=tenent_access_token)

        return res['data']

    def delete_bitable_view(self, tenent_access_token, app_token, table_id, view_id):
        """删除多维表格的table
        :type self: OpenLark
        :param tenent_access_token: tenent_access_token
        :type tenent_access_token: str
        :param app_token: 多维表格的 token
        :type app_token: str
        :param table_id: 多维表格的table_id
        :type table_id: str
        :param view_id_id: 多维表格的view_id
        :type view_id: str
        :rtype: dict
        删除多维表格的table
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-view/delete
        """
        url = f'https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/views/{view_id}'
        res = self._delete(url, with_token=tenent_access_token)

        return res['data']

    def add_bitable_field(self, tenent_access_token, app_token, table_id, field_name, field_type=1):
        """增加多维表格的field字段
        :type self: OpenLark
        :param tenent_access_token: tenent_access_token
        :type tenent_access_token: str
        :param app_token: 多维表格的 token
        :type app_token: str
        :param field_name: 多维表格的 field_name
        :type field_name: str
        :param field_type: field_name类型
        :type field_type: int
        :param table_id: 增加多维表格的field字段
        :type table_id: str
        :rtype: dict
        增加多维表格的table
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/create
        """
        url = f'https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/fields'
        body = {
            'field_name': field_name,
            'type': field_type
        }
        res = self._post(url, body=body, with_token=tenent_access_token)

        return res['data']

    def get_bitable_field_list(self, tenent_access_token, app_token, table_id):
        """获取多维表格的field列表
        :type self: OpenLark
        :param tenent_access_token: tenent_access_token
        :type tenent_access_token: str
        :param app_token: 多维表格的 app_token
        :type app_token: str
        :param table_id: 多维表格的 table_id
        :type table_id: str
        :rtype: list
        该接口用于获取多维表格的field列表
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/list
        """
        url = f'https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/fields'
        res = self._get(url, with_token=tenent_access_token)

        return res['data']['items']

    def delete_bitable_field(self, tenent_access_token, app_token, table_id, field_id):
        """删除多维表格的table
        :type self: OpenLark
        :param tenent_access_token: tenent_access_token
        :type tenent_access_token: str
        :param app_token: 多维表格的 token
        :type app_token: str
        :param table_id: 多维表格的table_id
        :type table_id: str
        :param field_id: 多维表格的field_id
        :type field_id: str
        :rtype: dict
        删除多维表格的table
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/delete
        """
        url = f'https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/fields/{field_id}'
        res = self._delete(url, with_token=tenent_access_token)

        return res['data']

    def update_bitable_field(self, tenent_access_token, app_token, table_id, field_id, field_name, field_type=1):
        """增加多维表格的field字段
        :type self: OpenLark
        :param tenent_access_token: tenent_access_token
        :type tenent_access_token: str
        :param app_token: 多维表格的 token
        :type app_token: str
        :param field_id: 多维表格的 field_id
        :type field_id: str
        :param field_type: field_type类型
        :type field_type: int
        :param field_name: field_name类型
        :type field_name: int
        :param table_id: 增加多维表格的field字段
        :type table_id: str
        :rtype: dict
        增加多维表格的table
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/update
        """
        url = f'https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/fields/{field_id}'
        body = {
            'field_name': field_name,
            'type': field_type
        }
        res = self._put(url, body=body, with_token=tenent_access_token)

        return res['data']

    def add_bitable_many_record(self, tenent_access_token, app_token, table_id, record):
        """新增多条记录
        :type self: OpenLark
        :param tenent_access_token: tenent_access_token
        :type tenent_access_token: str
        :param app_token: 多维表格的 token
        :type app_token: str
        :param record: 多维表格的record
        :type record: record
        :param table_id: 增加多维表格的field字段
        :type table_id: str
        :rtype: dict

        新增多条记录
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/batch_create
        """
        url = f'https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records/batch_create'
        body = {
            'records': record
        }
        res = self._post(url, body=body, with_token=tenent_access_token)

        return res['data']

    def delete_bitable_one_record(self, tenent_access_token, app_token, table_id, record_id):
        """该接口用于删除数据表中的一条记录
        :type self: OpenLark
        :param tenent_access_token: tenent_access_token
        :type tenent_access_token: str
        :param app_token: 多维表格的 token
        :type app_token: str
        :param table_id: 多维表格的table_id
        :type table_id: str
        :param field_id: 多维表格的field_id
        :type field_id: str
        :rtype: dict
        该接口用于删除数据表中的一条记录
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/delete
        """
        url = f'https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records/{record_id}'
        res = self._delete(url, with_token=tenent_access_token)

        return res['data']

    def get_bitable_record_list(self, tenent_access_token, app_token, table_id):
        """列出记录
        :type self: OpenLark
        :param tenent_access_token: tenent_access_token
        :type tenent_access_token: str
        :param app_token: 多维表格的 app_token
        :type app_token: str
        :param table_id: 多维表格的 table_id
        :type table_id: str
        :rtype: list
        列出记录
        https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/list
        """
        url = f'https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records'
        res = self._get(url, with_token=tenent_access_token)

        return res['data']['items']