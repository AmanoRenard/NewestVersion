# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

VERSIONS = {
    "ExpressCommand": {"version": "20250404", "msg": "版本已更新（20250407）：1.修复了极兔修改位置错误的BUG；2.修复了自动复制不全仍发出的BUG"}
}

@app.route('/get_version', methods=['GET'])
def get_version():
    app_name = request.args.get('name')
    if not app_name:
        return jsonify({"error": "Missing 'name' parameter"}), 400
    
    if app_name in VERSIONS:  # 直接使用原始的 VERSIONS 字典
        return jsonify(VERSIONS[app_name])  # 直接从字典中获取值
    else:
        return jsonify({"error": f"App '{app_name}' not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)