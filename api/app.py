# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
import json

app = Flask(__name__)

VERSIONS = {
    "ExpressCommand": {"version": "20250404", "msg": "版本已更新（20250407）：1.修复了极兔修改位置错误的BUG；2.修复了自动复制不全仍发出的BUG"}
}

@app.route('/get_version', methods=['GET'])
@app.route('/<app_name>', methods=['GET'])
def get_version(app_name=None):
    if not app_name:
        app_name = request.args.get('name')
    if not app_name:
        return jsonify({"error": "我思故我思。"}), 400
    
    if app_name in VERSIONS:
        return jsonify(VERSIONS[app_name], ensure_ascii=False)
    else:
        return jsonify({"error": f"App '{app_name}' not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)