from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
app = Flask(__name__)

api = 'http://service4:5001'


def new_register (generated):
        for key, value in generated.items(): 
            return key, value
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:root@34.68.21.59/flaskdb'
db = SQLAlchemy(app)
class Duo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal= db.Column(db.String(30), nullable=False)
    prize = db.Column(db.String(30), nullable=False)
db.create_all() 


@app.route('/')
def hello_internet():
    
    response = requests.get(api)
    generated = response.json() 
    print (generated)
    print(type(generated))
    animal, prize = new_register (generated)

    db.session.add(Duo(animal=animal, prize=prize))
    db.session.commit()
    
    final = Duo.query.all()
    for i in final: 
        animal1 = i.animal
        prize1 = i.prize 
    return render_template ( "base.html" , gn = (animal1, prize1))
    
    
    
if __name__=='__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')

