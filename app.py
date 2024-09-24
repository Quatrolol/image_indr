from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os

app = Flask(__name__)

@app.route('/generate-image', methods=['POST'])
def generate_image():
    text1 = request.form.get('text1', 'Default Text 1')
    text2 = request.form.get('text2', 'Default Text 2')
    
    template = Image.open('template.png')
    draw = ImageDraw.Draw(template)
    
    font = ImageFont.truetype('/app/font.ttf', size=24)
    
    draw.text((100, 400), text1, font=font, fill=(0, 0, 0))
    draw.text((100, 450), text2, font=font, fill=(0, 0, 0))
    
    img_io = BytesIO()
    template.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
