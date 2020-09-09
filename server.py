from flask import Flask, request, redirect, render_template
import numpy as np
import random
from tensorflow.keras.models import load_model
from PIL import Image


app = Flask(__name__)

#app.secret_key = "counter=0"
app.secret_key = "counter=0"

message = 'png, jpeg and jpg files only'


@app.route("/")
def index():
    return render_template('index.html', message=message)


ALLOWED_EXTENSIONS = (".jpg", ".jpeg", ".png")


model = load_model("static/model/weights.hdf5")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    files = request.files.getlist('uploadFile')
    labels = {0: 'desert', 1: 'plant', 2: 'water'}
    prediction = []
    image = []
    
    if len(files) > 10:
        return redirect('/', message="Upload less than 10 fiels every time")

    for file in files:
        if not file.filename.endswith(ALLOWED_EXTENSIONS):
            continue
        img = Image.open(file)
        img = img.resize((256, 256))
        image.append(img)
        img = np.asarray(img, dtype=np.float32)
        img = img / 255
        img = img[..., :3]
        img = img.reshape(-1, 256, 256, 3)
        predict = model.predict(img)
        predict = np.argmax(predict)
        prediction.append(labels[predict])

# uploaded images are in 'image' variable  of type list ,..... بديهيات
# predictions of images are in 'prediction' variable of type list ....., بديهيات 2

    return render_template('index.html', message=prediction)


app.run(
  debug=False,
  host='0.0.0.0',  
  port=random.randint(2000, 9000)
  )
