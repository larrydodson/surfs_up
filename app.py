# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello_worlds():
#     return 'Hello worlds'

# Sect 9.5.1 Set up db and Flask
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# to access and query the SQLite database file
engine = create_engine("sqlite:///hawaii.sqlite")
# to reflect the database
Base.prepare(engine, reflect=True)
# create a variable for each of the classes to reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station
# create a session link from Python to the database
session = Session(engine)

# define the Flask app, create a Flask application app
app = Flask(__name__)

# Sect 9.5.2 



