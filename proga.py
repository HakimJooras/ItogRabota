import tensorflow as tf
from flask import Flask, render_template, request
from tensorflow import keras
import numpy as np


app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def prediction():
    depth = ''
    width = ''
    if request.method == 'POST':
        IW = request.form.get('IW')
        IF = request.form.get('IF')
        VW = request.form.get('VW')
        FP = request.form.get('FP')

        paramet = [[float(IW), float(IF), float(VW), float(FP)]]

        model_loaded = tf.keras.models.load_model("model_1")
        pred = model_loaded.predict(paramet)

        depth = f"Глубина шва {pred[0][0]}"
        width = f"Ширина шва {pred[0][1]}"


    return render_template('index.html', depth=depth, width=width)

if __name__ == '__main__':
    app.run(debug=True)