from flask import request, send_file
import qrcode
from io import BytesIO

def generate_qr_route():
    data = request.form["data"]
    img = qrcode.make(data)
    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return send_file(buf, mimetype="image/png", as_attachment=True, download_name="qrcode.png")