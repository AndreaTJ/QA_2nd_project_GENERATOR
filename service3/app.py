from flask import Flask, render_template, jsonify
app = Flask(__name__)

import requests
api = 'http://localhost:5000'
api2 = 'http://localhost:5001'

@app.route('/')
def hello_internet():
    
    response = requests.get(api)
    print ("first api", response)
    print (response.text)
    first = response.text 

  

    response = requests.get(api2)
    print ("second api", response)
    print (response.text)

    second = response.text 

    generated = dict() 
    generated = {first:second}
    generated = jsonify (generated)
    return generated

if __name__=='__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')