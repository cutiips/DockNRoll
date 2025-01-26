from flask import Flask, request, jsonify

app = Flask(__name__)

# example
VALID_PASSWORD = "12345"

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    if data.get("password") == VALID_PASSWORD:
        return jsonify({"success": True, "message": "Accès autorisé"})
    return jsonify({"success": False, "message": "Mot de passe incorrect"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
