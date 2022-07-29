# Program to Upload Color Image and convert into Black & White image
import os
from flask import  Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import cv2
import numpy as np

app = Flask(__name__)

# Write load_form function below to Open and redirect to default upload webpage
@app.route('/')
def load():
    return render_template('index.html')

# Write upload_image Function to upload image and redirect to new webpage
@app.route('/gray', methods=['post'])
def upload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    data = greyscale(file.read())
    with open(os.path.join('static/', filename), 'wb') as f:
        f.write(data)
    
    message = "Image Uploaded !"

    return render_template('index.html', message=message, filename=filename)

def greyscale(image):
    img_array = np.fromstring(image, dtype='uint8')
    print('Image Array -', img_array)

    # Decode The Array Into A image
    decode_arr = cv2.imdecode(img_array, cv2.IMREAD_UNCHANGED)
    print('Decoded Array -', decode_arr)

    # Converting into greyscale
    convert = cv2.cvtColor(decode_arr, cv2.COLOR_RGB2GRAY)
    status, output = cv2.imencode('.PNG', convert)
    print('Status -', status)

    return output

# Write display_image Function to display the uploaded image
@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))

if __name__ == "__main__":
    app.run()