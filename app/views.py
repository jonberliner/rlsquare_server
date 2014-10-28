from flask import redirect, render_template, request, jsonify
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/next', methods = ['POST'])
def next():
    kwargs = request.json
    if not kwargs: redirect('/')
    else:
        view_time = kwargs.get('view_time')
        print view_time

        #TODO: generate RLsquare params

    return jsonify({})

