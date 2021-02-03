"""Main app/routing for med-cabinet"""
from flask import Flask, render_template, request
from .cannabis import *
# from .predict import predict


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html', effects=EFFECTS)


    @app.route('/prediction', methods=['POST'])
    def prediction():
        effects = request.form.getlist('effects')
        strain_type = request.form.get('type')

        strains = find_effects(effects, strain_type)

        values = parse_json(strains)
        
        # description = request.form.get('description')
        # prediction = predict(description)

        # top_10 = []
        # for i in prediction:
        #     top_10.append(find_index(i))
        
        return render_template('prediction.html', values=values)

    
    @app.route('/results', methods=['POST'])
    def results(): 
        search = request.form.get('search')
        values = search_strains(search)
        
        return render_template('results.html', values=values, search=search)


    @app.route('/search')
    def search():
        return render_template('search.html')

    
    @app.route('/about')
    def about():
        return render_template('about.html')       

    return app
