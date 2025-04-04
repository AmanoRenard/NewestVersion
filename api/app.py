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
    
    versions = json.dumps(VERSIONS)
    
    if app_name in versions:
        return jsonify({
            "app": app_name,
            "version": versions[app_name]
        })
    else:
        return jsonify({"error": f"App '{app_name}' not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)