from flask import Flask, request, jsonify
import subprocess, tempfile, os

app = Flask(__name__)

@app.route("/ocr", methods=["POST"])
def ocr():
    if "file" not in request.files:
        return jsonify(error="Upload an image in 'file' field"), 400
    f = request.files["file"]
    with tempfile.TemporaryDirectory() as tmpdir:
        src = os.path.join(tmpdir, "img")
        out = os.path.join(tmpdir, "out")
        f.save(src)
        # Run tesseract, output to stdout
        result = subprocess.run(["tesseract", src, "stdout"], capture_output=True, text=True)
        if result.returncode != 0:
            return jsonify(error=result.stderr), 500
        return jsonify(text=result.stdout)
