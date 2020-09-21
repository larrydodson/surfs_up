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
Base = automap_base()

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
# define the welcome route
@app.route("/")

# add the routing information for each of the other routes, create a function.
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Sect 9.5.3. next route 
@app.route("/api/v1.0/precipitation")

# precipitation function
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
     filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Sect 9.5.4. Stations route.
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Sect 9.5.5., Monthly Temperature route.
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Sect 9.5.6. Statistics route.
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]           

    if not end: 
     results = session.query(*sel).\
     filter(Measurement.date <= start).all()
     temps = list(np.ravel(results))
     return jsonify(temps)

    results = session.query(*sel).\
    filter(Measurement.date >= start).\
    filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)