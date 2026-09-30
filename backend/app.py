from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

# Folder where uploaded files will be stored
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return "ForenSight AI Backend is Working!"
@app.route("/upload", methods=["POST"])
def upload_file():

    # Check if a file was sent
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]

    # Check if a file was selected
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    # Make the filename safe
    filename = secure_filename(file.filename)

    # Create the file path
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    # Save the uploaded file
    file.save(file_path)

    return jsonify({
        "message": "File uploaded successfully",
        "filename": filename
    })
if __name__ == "__main__":
    app.run(debug=True)