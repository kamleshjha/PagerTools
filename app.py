from flask import Flask, render_template, request, send_file
from tools.text_to_speech import text_to_speech_route
from tools.qr_code import generate_qr_route
from tools.password_generator import generate_password_route
from tools.unit_converter import convert_unit_route
from tools.image_compressor import compress_image_route
from tools.pdf_to_text import pdf_to_text_route

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# Text to Speech
@app.route("/text-to-speech", methods=["POST"])
def text_to_speech():
    return text_to_speech_route()

# QR Code Generator
@app.route("/generate-qr", methods=["POST"])
def generate_qr():
    return generate_qr_route()

# Password Generator
@app.route("/generate-password", methods=["POST"])
def generate_password():
    return generate_password_route()

# Unit Converter
@app.route("/convert-unit", methods=["POST"])
def convert_unit():
    return convert_unit_route()

# Image Compressor
@app.route("/compress-image", methods=["POST"])
def compress_image():
    return compress_image_route()

# PDF to Text
@app.route("/pdf-to-text", methods=["POST"])
def pdf_to_text():
    return pdf_to_text_route()

if __name__ == "__main__":
    app.run(debug=True)