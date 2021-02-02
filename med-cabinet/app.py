"""Main app/routing for med-cabinet"""
from flask import Flask, render_template, request
from .cannabis import *


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html', effects=EFFECTS)


    @app.route('/prediction', methods=['POST'])
    def prediction():
        print(request.form.getlist('effects'))
        print(request.form.get('type'))
        print(request.form.get('description'))
        return render_template('prediction.html')

    
    @app.route('/results', methods=['POST'])
    def results(): 
        values = search_strains(request.form.get('search'))
        return render_template('results.html', values=values)


    @app.route('/search')
    def search():
        return render_template('search.html')

    
    @app.route('/about')
    def about():
        return render_template('about.html')       

    return app
