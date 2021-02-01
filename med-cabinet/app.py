"""Main app/routing for med-cabinet"""
from flask import Flask, render_template
from .cannabis import *


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return render_template('index.html')


    @app.route('/predict', methods=['POST'])
    def predict():
        return render_template('predict.html')

    
    @app.route('/about')
    def about():
        return render_template('about.html')       

    return app
