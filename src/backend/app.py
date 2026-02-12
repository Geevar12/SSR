import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Lazy-loaded globals
model = None
tokenizer = None

@app.route("/predict", methods=["POST"])
def predict():
    global model, tokenizer

    if model is None:
        from .model_loader import load_model
        model, tokenizer = load_model()

    if "video" not in request.files:
        return jsonify({"error": "No video uploaded"}), 400

    file = request.files["video"]
    path = "uploaded_video.mp4"
    file.save(path)

    from .model_loader import infer_video
    prediction = infer_video(path, model, tokenizer, beam_width=15)

    return jsonify({"prediction": prediction})


@app.route("/")
def health():
    return "SSR Backend Running"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
