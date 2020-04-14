# ----------------------------------------------------------------------- #

# CoronaTracker

# File:         application.py
# Maintainer:   DP Team
# Last Updated: 2020-04-13
# Language:     Python 3.7

# ------------------------------------------------------------------------ #

# ------------------------------------------------------------------------ #
# Initialization
# ------------------------------------------------------------------------ #

# Path
# ---------------------------------------------#
import os, sys
app_root = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))   

# Load external dependencies
# ---------------------------------------------#
## Flask Dependencies
import flask 

# Load internal dependencies
# ---------------------------------------------#
sys.path.append(os.path.normpath(os.path.join(app_root,'Backend')))
from DataProcessing import *

# Initialize the application
# ---------------------------------------------#
application = flask.Flask(__name__, 
	template_folder = os.path.join(app_root, 'Frontend'), 
	static_folder =os.path.join(app_root, 'Frontend'))

# ------------------------------------------------------------------------ #
# Define Views
# ------------------------------------------------------------------------ #

# home
# ---------------------------------------------#
@application.route('/home')
def home_view():

	# Generate the summary statistics
	summary_data = summary_corona_data()

	# Render the home page
	return flask.render_template('Home.html', infection_total = summary_data[0], 
		death_total = summary_data[1], country_list = summary_data[2] )
	
	
# update_owncountry
# ---------------------------------------------#
@application.route('/update_owncountry')
def update_owncountry_view():

	# Retrieve the location-specific data
	location_data = location_corona_data(longitude = flask.request.args.get('longitude'), 
		latitude = flask.request.args.get('latitude'))

	# Pass the data to the home page
	return flask.jsonify({"infection":location_data[0], "death":location_data[1], "country":location_data[2]})
 
# update_selectcountry
# ---------------------------------------------#
@application.route('/update_selectcountry')
def update_selectcountry_view():

	# Retrieve the location-specific data
	location_data = location_corona_data(country = flask.request.args.get('country'))

	# Pass the data to the home page
	return flask.jsonify({"infection":location_data[0], "death":location_data[1]})

# ------------------------------------------------------------------------ #
# Launch the Flask application
# ------------------------------------------------------------------------ #

if __name__ == "__main__":
	application.run()

# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
