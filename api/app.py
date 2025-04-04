from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

def load_versions():
    # 获取当前文件的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, '../../my_app_version.json')
    
    with open(json_path, 'r') as f:
        return json.load(f)

@app.route('/get_version', methods=['GET'])
def get_version():
    app_name = request.args.get('name')
    if not app_name:
        return jsonify({"error": "Missing 'name' parameter"}), 400
    
    versions = load_versions()
    
    if app_name in versions:
        return jsonify({
            "app": app_name,
            "version": versions[app_name]
        })
    else:
        return jsonify({"error": f"App '{app_name}' not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)