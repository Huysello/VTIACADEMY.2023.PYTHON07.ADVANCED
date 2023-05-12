import flask
print(flask.__version__)

# import libraries
from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
# Create an instance of the flask app
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World'

# if __name__ == '__main__':
#     app.run()

#configure our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    