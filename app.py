import os, tempfile, subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/")
def ping():
    return "ok"

@app.post("/ocr")
def ocr():
    if "file" not in request.files:
        return jsonify(error="Upload a file in form-data field 'file'"), 400
    f = request.files["file"]
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        f.save(tmp.name)
        result = subprocess.run(["tesseract", tmp.name, "stdout"],
                                capture_output=True, text=True)
    if result.returncode != 0:
        return jsonify(error=result.stderr), 500
    return jsonify(text=result.stdout)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
