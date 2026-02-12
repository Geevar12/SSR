import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from model_loader import load_model, infer_video

app = Flask(__name__)
CORS(app)

# Lazy loading (do NOT load at startup)
model = None
tokenizer = None


@app.route("/predict", methods=["POST"])
def predict():
    global model, tokenizer

    # Load model only on first request
    if model is None or tokenizer is None:
        model, tokenizer = load_model()

    if "video" not in request.files:
        return jsonify({"error": "No video uploaded"}), 400

    file = request.files["video"]
    path = "uploaded_video.mp4"
    file.save(path)

    prediction = infer_video(path, model, tokenizer, beam_width=15)

    return jsonify({"prediction": prediction})


# Required for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
