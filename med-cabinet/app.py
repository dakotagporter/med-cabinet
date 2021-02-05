"""Main app/routing for med-cabinet"""
from flask import Flask, render_template, request, url_for, redirect, flash
from .cannabis import *
from .predict import predict


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key-goes-here'

    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html', effects=EFFECTS)

    @app.route('/results')
    def results():
        return render_template('results.html')

    @app.route('/results', methods=['POST'])
    def results_post():
        if request.method == 'POST':
            error = None
            # Retrieve user input
            effects = request.form.getlist('effects')
            # Retrieve user search input
            search = request.form.get('search')

            if search:
                # Search strains based on input
                values = search_strains(search)
                
                if values == ERROR:
                    values = ''
                    error = ERROR
                
                return render_template('results.html', values=values, search=search, error=error)

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


        return render_template('results.html', strains=strains)

    @app.route('/search')
    def search():
        return render_template('search.html')

    @app.route('/about')
    def about():
        # TODO: Display author information
        return render_template('about.html')

    return app
