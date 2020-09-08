import io
import os
import random
from flask import Flask, flash, request, redirect, url_for, render_template , Response
from werkzeug.utils import secure_filename
import sys

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2
from tensorflow.keras.layers import *
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.initializers import glorot_uniform
from tensorflow.keras.utils import plot_model
from IPython.display import display
from tensorflow.keras import backend as K
import PIL
from PIL import Image


app = Flask(__name__)

app.secret_key = "counter=0"

UPLOAD_FOLDER = 'static/upload/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# a route where we will display a welcome message via an HTML template
message = 'png, jpeg and jpg files only'


@app.route("/")
def index():
    return render_template('index.html', message=message)




@app.route('/predict', methods=['GET', 'POST'])
def predict():
    files = request.files.getlist('uploadFile')

    labels = {0: 'desert', 1: 'plant', 2: 'water'}
    
    # Loading the model weights 
    model = load_model('static/model/weights.hdf5')
    
    prediction = []
    image = []

    # if there is more than 10 uploaded images don't continue and return with this message ,.... مش وكالة من غير بواب هي 
    if len(files) > 10 :
        return redirect('/' , message = "Upload less than 10 fiels every time")

    for file in files:
        if file and allowed_file(file.filename):
            filename = file.filename
            img = PIL.Image.open(file)
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


# temp output display of one image 
    message = prediction[0]

    return render_template('index.html', message = message)




if __name__ == "__main__":
    app.run(  
        debug=True,
        host='0.0.0.0',  
        port=random.randint(2000, 9000)
    )
