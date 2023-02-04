from flask import Flask, jsonify, request, make_response
import qrcode
from io import BytesIO
import io

app = Flask(__name__)

@app.route('/qr-code', methods=['GET'])
def generate_qr_code():
    url = request.args.get('url')
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    response = make_response(buffer.getvalue())
    response.headers.set('Content-Type', 'image/png')
    response.headers.set(
        'Content-Disposition', 'attachment', filename='qrcode.png')
    return response
   

if __name__ == "__main__":
    app.run()