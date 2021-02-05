from flask import Flask, render_template, request, flash
from .cannabis import EFFECTS, ERROR, search_strains, query_results
from .predict import predict


def create_app():
    """
    This function is the foundation for the Flask API of this project. This
    function is a cumulation of all application endpoints and configurations.
    """
    app = Flask(__name__)

    # App configurations
    app.config['SECRET_KEY'] = 'secret-key-goes-here'

    # App endpoints
    @app.route('/', methods=['GET'])
    def index():
        """
        Application home page using the base html file.
        """
        return render_template('index.html', effects=EFFECTS)

    @app.route('/results')
    def results():
        """
        Renders results html template to provide search results for users.
        """
        return render_template('results.html')

    @app.route('/results', methods=['POST'])
    def results_post():
        """
        Deals with any POST methods returned from the base html page.
        """
        if request.method == 'POST':
            error = None
            # Retrieve user input
            effects = request.form.getlist('effects')
            # Retrieve user search input
            search = request.form.get('search')

            # Search and return strains if user search parameters are provided
            if search:
                values = search_strains(search)

                if values == ERROR:
                    values = ''
                    error = ERROR

                return render_template('results.html', values=values,
                                       search=search, error=error)

            # Return an error if no effects are chosen by user
            if not effects:
                flash('Please choose at least one effect')
                return render_template('index.html', effects=EFFECTS,
                                       error=True)

            # Retrieve strain_type if provided by user
            strain_type = request.form.get('type')
            # Retrieve description if provided by user
            description = request.form.get('description')

            # Run model if user description is provided
            if description != '':
                # Get strain indices based on user description
                prediction = predict(description)
                # Search strains based on user's chosen effects and strain type
                strains = query_results(effects, strain_type, prediction)
            else:
                # Search strains based on user's chosen effects and strain type
                strains = query_results(effects, strain_type, None)

        return render_template('results.html', strains=strains)

    @app.route('/search')
    def search():
        """
        Renders search page for users to search strains by name.
        """
        return render_template('search.html')

    @app.route('/about')
    def about():
        """
        Display information about project and authors in the about html page.
        """
        return render_template('about.html')

    return app
