from flask import Flask
import random
app = Flask(__name__)

############################
@app.route('/')
def prizes():
    prizes = dict() 
    prizes = {1:100, 2:10, 3:200, 4:34, 5:500, 6:780, 7:300, 8:430, 9:3, 10: 0.4}
    number = random.randint (1, len(prizes.keys()))
    return str(prizes[number])


