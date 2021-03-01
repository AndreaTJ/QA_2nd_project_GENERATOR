from flask import Flask
import random
app = Flask(__name__)

##############################################

@app.route('/')
def hello_internet():
    destination = "anywhere"

    return destination



