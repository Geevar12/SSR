import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Point Flask to React build folder
app = Flask(
    __name__,
    static_folder="../../dist",
    static_url_path=""
)

CORS(app)

# Lazy-loaded globals
model = None
tokenizer = None


# ---------------- API ROUTE ----------------
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


# ---------------- FRONTEND ROUTES ----------------
@app.route("/")
def serve_react():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/<path:path>")
def serve_static(path):
    file_path = os.path.join(app.static_folder, path)
    if os.path.exists(file_path):
        return send_from_directory(app.static_folder, path)
    else:
        # React Router fallback
        return send_from_directory(app.static_folder, "index.html")


# ---------------- START SERVER ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
