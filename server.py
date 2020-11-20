from flask import Flask, request, redirect, url_for,Response,render_template,send_file,make_response,jsonify,send_from_directory

import base64
import io
from PIL import Image
# Initialize the Flask application
app = Flask(__name__)


@app.route("/resize_image", methods=["POST"])
def process_image():
    payload = request.form.to_dict(flat=False)

    im_b64 = payload['input_jpeg'][0]
    width = payload['desired_width']
    height = payload['desired_height']
    desired_size = int(width[0]), int(height[0])
    im_binary = base64.b64decode(im_b64)
    buf = io.BytesIO(im_binary)
    img = Image.open(buf)
    new_img = img.resize(desired_size)
    new_img.save('image.jpeg')

    with open('image.jpeg', 'rb') as f:
        im_b64 = base64.b64encode(f.read())

    return jsonify({'code':'200', 'message':'success', 'output_jpeg':str(im_b64)})

# app.run(host="0.0.0.0", port=8080)