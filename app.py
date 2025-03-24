from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/read-text', methods=['POST'])
def read_text():
    data = request.json
    text = data.get("text", "")
    
    if not text:
        return jsonify({"error": "No text provided"}), 400

    return jsonify({"message": f"O texto recebido foi: {text}"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

