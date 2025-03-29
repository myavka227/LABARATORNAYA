from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/v1/contact', methods=['POST', 'GET', 'PUT', 'DELETE'])
def contact():
    return jsonify({})  # Заглушка

@app.route('/api/v1/group', methods=['POST', 'GET', 'PUT', 'DELETE'])
def group():
    return jsonify({})  # Заглушка

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6080)
