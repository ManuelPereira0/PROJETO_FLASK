from crypt import methods
import json
import pandas as pd
from flask_ngrok import run_with_ngrok
from flask import request
from flask import Flask
from flask import jsonify
app = Flask(__name__)
run_with_ngrok(app)

dados_input = [{
    'number': '1',
    'name': 'Mahesh',
    'age' : 25,
    'city': 'Bangalore',
    'country': 'India'
},
{
    'number': '2',
    'name': 'Alex',
    'age' : 26,
    'city': 'London',
    'country': 'UK'
},
{
    'number': '3',
    'name': 'David',
    'age' : 27,
    'city': 'San Francisco',
    'country': 'USA'
},
{
    'number': '4',
    'name': 'John',
    'age' : 28,
    'city': 'Torondo',
    'country': 'Canada'
},
{
    'number': '5',
    'name': 'Chris',
    'age' : 29,
    'city': 'Paris',
    'country': 'France'
}]

@app.route("/")

def home():
    return "Olá Mundo!"

@app.route("/input")

def input_route():
    return jsonify(dados_input)

app.run()