from flask import Flask, request
from app import app

# static url
@app.route('/')
def index():
    return "Hello, World!"

# url parameters
@app.route('/endpoint/<input>')
def endpoint(input):
    return input

# api with endpoint
@app.route('/nameEndpoint', methods=['GET'])
def nameEndpoint():
    if 'name' in request.args:
    	return 'My name is ' + request.args['name']
