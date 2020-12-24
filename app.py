from flask import Flask
from datetime import datetime
from  flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.now)
@app.route("/<name>")
def view(name):
    user=User.query.filter_by(name=name).first()
    return f'this is  name of user&nbsp; ={user.name}&nbsp;&nbsp;location of user= &nbsp;{user.location}&nbsp; and date={user.date_created} &nbsp;'
@app.route("/<name>/<location>")
def index(name,location):
    user=User(name=name,location=location)
    db.session.add(user)
    db.session.commit()
    return "<h1>Added new user!"



# ab.run()
if(__name__ == "__main__"):
    app.run(debug=True)