"""Main app/routing for med-cabinet"""
from flask import Flask, render_template, request, url_for, redirect, flash
from .cannabis import *
from .predict import predict


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key-goes-here'

    @app.route('/')
    def index():
        return render_template('index.html', effects=EFFECTS)

    @app.route('/prediction')
    def prediction():
        return render_template('prediction.html')

    @app.route('/prediction', methods=['POST'])
    def prediction_post():
        if request.method == 'POST':
            # Retrieve user input
            # TODO: Return error if effects or strain type is not provided
            effects = request.form.getlist('effects')
            if not effects:
                flash('Please choose at least one effect')
                return render_template('index.html', effects=EFFECTS,
                                       error=True)
            strain_type = request.form.get('type')
            # Retrieve description (if applicable)
            description = request.form.get('description')
            if not description == '':
                # Return indices of recommended strains based on user description
                prediction = predict(description)
            # Search strains based on user's chosen effects and strain type
                strains = query_results(effects, strain_type, prediction)
            else:
                strains = query_results(effects, strain_type, None)
            # Parse each strain to retrieve it's properties


        return render_template('prediction.html', top_10=strains, search=search)

    @app.route('/results', methods=['POST'])
    def results():
        # Retrieve user search input
        search = request.form.get('search')
        # Search strains based on input
        values = search_strains(search)

        return render_template('results.html', values=values, )

    @app.route('/search')
    def search():
        return render_template('search.html')

    @app.route('/about')
    def about():
        # TODO: Display author information
        return render_template('about.html')

    return app
