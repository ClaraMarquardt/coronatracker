# ----------------------------------------------------------------------- #

# CoronaTracker

# File:         DataProcessing.py
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
app_root = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))  

# Load external dependencies
# ---------------------------------------------#
## General Dependencies
import pandas as pd
import numpy as np

## Geocoding Dependencies
import geopy
from geopy.geocoders import Nominatim

# ------------------------------------------------------------------------ #
# Define Functions
# ------------------------------------------------------------------------ #

# summary_corona_data
# ---------------------------------------------#
def summary_corona_data(datapath = os.path.join(app_root, "Backend/Data/CoronaData.csv")):

	# Load the data
	corona_df = pd.read_csv(datapath, encoding="utf-8")

	# Obtain country list
	country_list = corona_df["country"]

	# Generate summary statistics
	infection_total = int(np.sum(corona_df["infection"]))
	death_total     = int(np.sum(corona_df["death"]))
	
	# Return the summary statistics
	return([infection_total, death_total, country_list])


# location_corona_data
# ---------------------------------------------#
def location_corona_data(longitude=None, latitude=None , country=None, datapath = os.path.join(app_root, "Backend/Data/CoronaData.csv")):

	# Load the data
	corona_df = pd.read_csv(datapath, encoding="utf-8")

	# Geocode the longitude/latitude data if not provided with country
	if (country == None):

		## Initialize the geocoder
		locator      = Nominatim(user_agent="myGeocoder")

		## Obtain the country
		coordinates  = str(latitude) + ", " + str(longitude)
		geocode_data = locator.reverse(coordinates)
		country      = geocode_data.raw['address']['country']

	# Subset to the location
	corona_location_df = corona_df[corona_df["country"]==country]

	# Generate location-specific statistics
	infection = int(np.sum(corona_location_df["infection"]))
	death     = int(np.sum(corona_location_df["death"]))

	# Return the summary statistics
	return([infection, death, country])

# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #

