from flask import Flask, render_template, jsonify
app = Flask(__name__)

import requests
api = 'http://flask-app-1:5003'
api2 = 'http://flask-app-2:5002'

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
    app.run(port=5001, debug=True, host='0.0.0.0')
