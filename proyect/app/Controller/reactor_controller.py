from flask import request
from flask import jsonify
from service.reactor_service import ReactorService
from model.reactor import Reactor


reactor_service = ReactorService()

def get_all_reactors():
    reactors = reactor_service.get_all_reactors()
    if reactors:
        return reactors
    else:
        return "Error al obtener todos los reactores"


def create_reactor():
    try:
        # Obtener los datos del reactor del cuerpo de la solicitud
        reactor_data = request.json
        # Crear una instancia de Reactor con los datos recibidos
        reactor = Reactor(**reactor_data)
        # Llamar al servicio para crear el reactor en la base de datos
        reactor_id = reactor_service.create_reactor(reactor)
        if reactor_id:
            return {"reactor_id": reactor_id}, 201
        else:
            return {"error": "Error al crear el reactor"}, 500
    except Exception as e:
        print("Error en la creación del reactor:", e)
        return {"error": "Error en la creación del reactor"}, 500
    
def get_reactor_by_id(reactor_id):
    reactor = reactor_service.get_reactor_by_id(reactor_id)
    if reactor:
        return jsonify(reactor.__dict__), 200
    else:
        return {"error": "No se encontró el reactor"}, 404