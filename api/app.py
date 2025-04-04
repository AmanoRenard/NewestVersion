from flask import Flask, jsonify, request
import json

app = Flask(__name__)

VERSIONS = {
    "ExpressCommand": "20250404",
    "test": "114514",
    "StoreOffline": "20250404"
}

@app.route('/get_version', methods=['GET'])
def get_version():
    app_name = request.args.get('name')
    if not app_name:
        return jsonify({"error": "Missing 'name' parameter"}), 400
    
    if app_name in VERSIONS:  # 直接使用原始的 VERSIONS 字典
        return jsonify({
            "version": VERSIONS[app_name]  # 直接从字典中获取值
        })
    else:
        return jsonify({"error": f"App '{app_name}' not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)