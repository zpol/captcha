from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from PIL import Image
import os

app = Flask(__name__, static_folder="static")
CORS(app)  # Enable CORS


os.makedirs(app.static_folder, exist_ok=True)

captcha_store = {}

@app.route('/generate_captcha', methods=['GET'])
def generate_captcha_route():
    """
    Genera un CAPTCHA y devuelve su URL.
    """
    from utils import generate_captcha
    captcha_text, captcha_image = generate_captcha()
    captcha_id = len(os.listdir(app.static_folder)) + 1
    captcha_path = os.path.join(app.static_folder, f"captcha_{captcha_id}.png")
    captcha_image.save(captcha_path)

    captcha_store[captcha_id] = captcha_text

    return jsonify({
        "captcha_id": captcha_id,
        "captcha_image_url": f"/static/captcha_{captcha_id}.png"
    })

@app.route('/verify_captcha', methods=['POST'])
def verify_captcha_route():
    """
    Verifica el texto del CAPTCHA.
    """
    data = request.json
    print('Received data:', data)
    captcha_id = data.get("captcha_id")
    user_input = data.get("user_input")

    correct_text = captcha_store.get(captcha_id)

    if correct_text and correct_text == user_input:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "error": "Incorrect CAPTCHA"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)