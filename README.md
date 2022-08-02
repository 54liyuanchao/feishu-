# 飞书常用接口的封装

## 使用示例

```shell
from larkbot import LarkBot
lark = LarkBot(app_id = APP_ID, app_secret = APP_SECRET)
file_key = lark.upload_file(filename, filepath=filepath)
lark.send_chat_file(CHAT_ID, file_key)
```

## API实现功能列表

- [ ] 授权
  - [x] 获取 app_access_token（企业自建应用）
- [ ] 群组
  - [x] 获取用户所在的群列表
  - [x] 获取群成员列表
  - [x] 搜索用户所在的群列表
- [ ] 
- [ ] 多维表格
- [ ] 机器人
  - [x] 批量发送消息
  - [x] 发送文本消息
  - [x] 发送图片消息
  - [x] 发送富文本消息
  - [x] 发送群名片
  - [x] 发送卡片通知
- [ ] 

- [x] 发送卡片通知

  