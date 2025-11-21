# -*- coding: utf-8 -*-
import os
from flask import Flask, send_from_directory

# Создаём Flask-приложение
app = Flask(__name__, static_url_path='', static_folder='.')

# Главная страница
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Статические файлы в корне (css, js, index.html, другие)
@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

# Файлы из папки data
@app.route('/data/<path:filename>')
def data_files(filename):
    return send_from_directory('data', filename)

# Файлы из папки images
@app.route('/images/<path:filename>')
def image_files(filename):
    return send_from_directory('images', filename)

# Запуск приложения
if __name__ == '__main__':
    # Render назначает порт через переменную окружения PORT
    port = int(os.environ.get('PORT', 10000))  # локально будет 10000
    app.run(debug=True, host='0.0.0.0', port=port)