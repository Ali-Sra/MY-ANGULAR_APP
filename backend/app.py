from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = 'messages.json'

@app.route('/')
def home():
    return '🚀 Flask Backend is Running!'

@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        print(f"New message from {name} ({email}): {message}")

        # ساختن ساختار JSON جدید
        new_message = {
            "name": name,
            "email": email,
            "message": message
        }

        # اگر فایل وجود داشت، بارگذاری کن، اگر نه، لیست خالی بساز
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                all_messages = json.load(f)
        else:
            all_messages = []

        # اضافه کردن پیام جدید
        all_messages.append(new_message)

        # ذخیره در فایل
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(all_messages, f, indent=2, ensure_ascii=False)

        return jsonify({
            'status': 'success',
            'msg': f'Thank you {name}, your message was saved!'
        })

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            'status': 'error',
            'msg': 'Something went wrong on the server!'
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
