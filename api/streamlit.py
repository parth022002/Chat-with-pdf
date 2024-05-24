import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Streamlit server is running."

@app.route('/run-streamlit', methods=['POST'])
def run_streamlit():
    port = request.json.get('port', 8501)
    process = subprocess.Popen(['streamlit', 'run', 'app.py', '--server.port', str(port)])
    return jsonify({"status": "started", "port": port, "pid": process.pid})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
