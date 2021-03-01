from flask import Flask
import random
app = Flask(__name__)

##############################################

@app.route('/')
def hello_internet():
    destination = "anywhere"

    return destination

if __name__=='__main__':
    app.run(port=5003, debug=True, host='0.0.0.0')

