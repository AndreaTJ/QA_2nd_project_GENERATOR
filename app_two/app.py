from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def hello_internet():
    prizes = dict() 
    prizes = {1:"car", 2:"house", 3:"money"}

    number = random.randint (1, len(prizes.keys()))


    return prizes[number] 

if __name__=='__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')
