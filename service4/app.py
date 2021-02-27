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

if __name__=='__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')