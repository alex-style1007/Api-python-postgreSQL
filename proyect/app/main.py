from flask import flask
from service.reactor_service import ReactorService
from service.location_service import LocationService
from Controller import reactor_controller
from Controller import location_controller 
from context.db_connection import connect_to_database

app=flask(__name__)

connection=connect_to_database()

reactor_service=ReactorService(connection)
location_service=LocationService(connection)

if __name__=='__main__':
    app.run(debug=True)

