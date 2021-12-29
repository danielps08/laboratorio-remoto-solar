import pyrebase
from flask import Flask, render_template, request, make_response,redirect, url_for
import json
from time import time
from random import random

config = {
    "apiKey": "AIzaSyApOH8UDyVn_FAC9swPGH1smcO3Hx0b2-s",
    "authDomain": "lab-remoto-solar.firebaseapp.com",
    "databaseURL": "https://lab-remoto-solar-default-rtdb.firebaseio.com",
    "projectId": "lab-remoto-solar",
    "storageBucket": "lab-remoto-solar.appspot.com",
    "messagingSenderId": "621925670253",
    "appId": "1:621925670253:web:51dd7ea82ecd033dca0e64",
    "measurementId": "G-3MDPK87N5D"    
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['sub'] == 'enviar':
            dato = request.form['angulo']
            db.child("flask").update({"angulo" : int(dato)})
        elif request.form['sub'] == 'on':
            db.child("estado").update({"led" : True})
        elif request.form['sub'] == 'off':
            db.child("estado").update({"led" : False})
        return render_template('index.html')
    return render_template('index.html')
    
@app.route('/data', methods=['GET', 'POST'])
def data():
    sensor = db.child("sensor").child("valor").get()
    valor = sensor.val()
    #Temperature = random() * 100
    #Humidity = random() * 55

    #data = [time() * 1000, Temperature, Humidity]
    data=[time() * 1000, valor]
    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response

if __name__ == '__main__':
    app.run(debug=True)
    
