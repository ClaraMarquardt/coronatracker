# ----------------------------------------------------------------------- #

# CoronaTracker

# File:         CoronaTracker.py
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

# Initialize the app
# ---------------------------------------------#
app = flask.Flask(__name__, 
	template_folder = os.path.join(app_root, 'Frontend/Templates'), 
	static_folder = os.path.join(app_root, 'Frontend/Static'))

# ------------------------------------------------------------------------ #
# Define Views
# ------------------------------------------------------------------------ #

# Home
# ---------------------------------------------#
@app.route('/home')
def home_view():

	# Generate the summary statistics
	summary_data = summary_corona_data()

	# Render the home page
	return flask.render_template('Home.html', infection_total = summary_data[0], 
		death_total = summary_data[1], country_list = summary_data[2] )
	
	
# Vis
# ---------------------------------------------#
@app.route('/vis')
def view_view():

	# Retrieve the location-specific data
	location_data = location_corona_data(flask.request.args.get('longitude', None), 
		flask.request.args.get('latitude', None), flask.request.args.get('country', None))

	# Pass the data to the home page
	return flask.jsonify({"infection":location_data[0], "death":location_data[1], "country":location_data[2]})
 
# ------------------------------------------------------------------------ #
# Launch the Flask app
# ------------------------------------------------------------------------ #
app.run()

# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
