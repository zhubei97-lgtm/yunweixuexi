import os
from flask import Flask

title = os.environ.get('title','Counter')
app = Flask(__name__)

COUNT_FILE = '/data/count.txt'

def get_count():
    if os.path.exists(COUNT_FILE):
        with open(COUNT_FILE, 'r') as f:
            return int(f.read().strip())
    return 0

def save_count(c):
    # 确保 /data 目录存在，如果不存在则创建
    os.makedirs(os.path.dirname(COUNT_FILE), exist_ok=True)
    with open(COUNT_FILE, 'w') as f:
        f.write(str(c))

@app.route('/')
def index():
    count = get_count()
    count += 1
    save_count(count)
    return f'{title} – Visits: {count} (Visits: v2.0)'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
