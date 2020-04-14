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

# Load internal dependencies
# ---------------------------------------------#
sys.path.append(os.path.normpath(os.path.join(app_root,'Backend')))
from DataProcessing import *

# ------------------------------------------------------------------------ #
# Test Functions
# ------------------------------------------------------------------------ #

# home
# ---------------------------------------------#
data = summary_corona_data()

print(data[0])
print(data[1])
print(data[2])

# update_owncountry
# ---------------------------------------------#
data = location_corona_data(longitude = -71.08328259999999, latitude = 42.3662154)

print(data[0])
print(data[1])
print(data[2])

# update_selectcountry
# ---------------------------------------------#
data = location_corona_data(country = "Germany")

print(data[0])
print(data[1])
print(data[2])

# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
