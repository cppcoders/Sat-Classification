from flask import Flask, request, redirect, render_template
import numpy as np
from PIL import Image
import base64
from io import BytesIO


app = Flask(__name__)

app.secret_key = "counter=0"

# a route where we will display a welcome message via an HTML template

message = "Home"


@app.route("/")
def index():
    return render_template('home.html', message="Home")


app.config["TEMPLATES_AUTO_RELOAD"] = True
ALLOWED_EXTENSIONS = (".jpg", ".jpeg", ".png")



@app.route('/predict', methods=['GET', 'POST'])
def predict():
    files = request.files.getlist('uploadFile')
    pred = {}
    if len(files) > 10:
        return redirect('/model')

    for file in files:
        if not file.filename.endswith(ALLOWED_EXTENSIONS):
            continue
        img = Image.open(file)
        img = img.resize((256, 256))
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        pim = base64.b64encode(buffered.getvalue())
        img = np.asarray(img, dtype=np.float32)
        img = img / 255
        img = img[..., :3]
        img = img.reshape(-1, 256, 256, 3)
        predict = "image"
        pred[pim] = predict
    return render_template('model.html', message=pred)


@app.route("/model")
def mod():
    return render_template('model.html', message="model")

@app.route("/documentation")
def doc():
    return render_template('documentation.html', message="doc")

@app.route("/user_manuals")
def user():
    return render_template('user_manuals.html', message="user")

@app.route("/about_us")
def about():
    return render_template('about_us.html', message="about")



if __name__ == '__main__':
    app.run()