from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "data.json"

#   读取留言
def load_messages():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

#   写入留言
def write_messages(messages):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)

#   获取全留言
@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(load_messages())

#   提交留言
@app.route('/message', methods=['POST'])
def post_message():
    data = request.get_json()
    if not data or 'name' not in data or 'content' not in data:
        return jsonify({'error': 'name 和 content 是必须的'}), 400

    new_msg = {
        'name': data['name'],
        'content': data['content'],
    }

    messages = load_messages()
    messages.append(new_msg)
    write_messages(messages)
    return jsonify({'message': '留言成功'}), 201

if __name__ == '__main__':
    app.run(port=5000, debug=True)
