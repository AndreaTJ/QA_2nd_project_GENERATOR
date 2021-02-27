from flask import Flask, render_template, jsonify
app = Flask(__name__)

import requests
api = 'http://service2:5001'
api2 = 'http://service3:5002'

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

