from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def hello_internet():
    animal = dict() 
    animal = {1:"bear", 2:"cat", 3:"dog"}

    number = random.randint (1, len(animal.keys()))
    doce = len(animal.keys())
    print(doce) 

    return animal[number] 

