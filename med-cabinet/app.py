"""Main app/routing for med-cabinet"""
from flask import Flask, render_template, request
from .cannabis import *
from .predict import predict


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html', effects=EFFECTS)

    @app.route('/prediction', methods=['POST'])
    def prediction():
        # Retrieve user input
        # TODO: Return error if effects or strain type is not provided
        effects = request.form.getlist('effects')
        strain_type = request.form.get('type')
        # Retrieve description (if applicable)
        description = request.form.get('description')

        # Search strains based on user's chosen effects and strain type
        strains = find_effects(effects, strain_type)
        # Parse each strain to retrieve it's properties
        values = parse_json(strains)
        # Return indices of recommended strains based on user description
        prediction = predict(description)

        # Retrieve strains based on index location
        top_10 = []
        for i in prediction:
            top_10.append(find_index(i))

        return render_template('prediction.html', top_10=top_10, values=values)

    @app.route('/results', methods=['POST'])
    def results():
        # Retrieve user search input
        search = request.form.get('search')
        # Search strains based on input
        values = search_strains(search)

        return render_template('results.html', values=values, search=search)

    @app.route('/search')
    def search():
        return render_template('search.html')

    @app.route('/about')
    def about():
        # TODO: Display author information
        return render_template('about.html')

    return app
