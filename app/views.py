from flask import redirect, render_template, request, jsonify
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/next', methods = ['POST'])
def next():
    kwargs = request.json
    print kwargs
    if kwargs:
        view_time = kwargs.get('view_time')
        print view_time

        #TODO: generate RLsquare params
        params = {'h1': 255.0,
                  'h2': 51.0,
                  'oscTime': 7000.0,
                  's1': 255.0,
                  's2': 255.0,
                  'sigSteepness': 0.75,
                  'v1': 68.0,
                  'v2': 221.0}

        return jsonify(params)
    redirect('/')

