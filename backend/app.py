from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timezone

app = Flask(__name__)
CORS(app)


@app.get('/health')
def health():
    return jsonify({'status': 'ok'})


@app.get('/tasks')
def get_tasks():
    return jsonify(
        {
            'system': 'Cloud-Native Task Monitor',
            'generated_at': datetime.now(timezone.utc).isoformat(),
            'tasks': [
                {'task': 'Database Backup', 'status': 'Complete'},
                {'task': 'Security Patch Scan', 'status': 'In Progress'},
                {'task': 'Log Rotation', 'status': 'Complete'},
            ],
        }
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
