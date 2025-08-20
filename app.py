import os, json
from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_folder='static')

# Serve index
@app.route('/')
def root():
    return send_from_directory('.', 'index.html')

# Images
@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('images', filename)

# API endpoint
@app.route('/api/yeti')
def api_yeti():
    with open('database/yeti_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

# Health check
@app.route('/health')
def health():
    return {'status': 'ok'}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
