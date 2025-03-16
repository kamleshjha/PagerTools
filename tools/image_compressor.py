from flask import request, send_file
from PIL import Image
import io

def compress_image_route():
    file = request.files["image"]
    img = Image.open(file)
    img = img.convert("RGB")
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=50)
    buf.seek(0)
    return send_file(buf, mimetype="image/jpeg", as_attachment=True, download_name="compressed.jpg")