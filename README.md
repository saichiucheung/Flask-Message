Flask 留言功能 API（无数据库版）

这是一个使用 Python 和 Flask 实现的简易留言系统，适合学习和轻量级项目使用。数据保存在本地 JSON 文件中，不依赖数据库。

一、功能说明：

-    获取所有留言（GET /messages）

-    提交新留言（POST /messages）

-    使用本地 JSON 文件作为数据存储

-    适合初学者练习后端 API 开发

二、项目结构：

```
flask-message/
├── app.py              # Flask 应用主文件
├── messages.json       # 本地留言数据文件
├── requirements.txt    # 依赖说明
├── README.md           # 项目说明文档
```

三、环境准备

1. 安装 Python 3 及其以上版本

2. 安装依赖

```
pip install flask
```

或使用 requirements.txt

```
pip install -r requirements.txt
```

四、启动服务：

在项目根目录下运行

```
python app.py
```

访问地址为

```
http://127.0.0.1:5000
```

五、接口说明：

-    GET /messages

```
[
  {
    "name": "示例用户",
    "content": "留言内容"
  }
]
```

-    POST /messages

```
{
  "name": "你的名字",
  "content": "留言内容"
}
```

-    成功响应：

```
{
  "status": "success"
}
```

-    失败响应：

```
{
  "error": "name 和 content 是必须的"
}
```

六、示例请求（使用 curl）

```
curl -X POST http://127.0.0.1:5000/messages \
  -H "Content-Type: application/json" \
  -d "{\"name\": \"秋城\", \"content\": \"你好，这是我的留言\"}"
```

七、注意事项

-    当前项目使用本地文件存储，不适合线上高并发部署。

-    可根据需要扩展为使用 SQLite 或 MySQL 数据库。
