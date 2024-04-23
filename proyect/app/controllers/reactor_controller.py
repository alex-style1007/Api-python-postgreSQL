from typing import List
from fastapi import FastAPI, status, Path, Query, Body, Depends
from models.reactor_schema import ReactorResponseModel
from services.reactor_service import ReactorService
from utils.utils import get_session


app = FastAPI()

@app.get(
        path='/reactor',
        status_code=status.HTTP_200_OK,
        response_model=List[ReactorResponseModel],
)
async def get_reactores(session = Depends(get_session)):
    return ReactorService().get_all_reactors()


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

def get_all_types_reactor():
    reactor_types = reactor_service.get_all_types_reactor()
    if reactor_types:
        return jsonify(reactor_types), 200
    else:
        return {"error": "Error al obtener los tipos de reactores"}, 500
    
def get_reactors_by_type_id(reactor_id):
    reactor = reactor_service.get_reactors_by_type_id(reactor_id)
    if reactor:
        return jsonify(reactor.__dict__), 200
    else:
        return {"error": "No se encontraron reactores asociados a este tipo de reactor"}, 404

def delete_reactor(reactor_id):
    success = reactor_service.delete_reactor(reactor_id)
    if success:
        return {"message": "Reactor eliminado exitosamente"}, 200
    else:
        return {"error": "Error al eliminar el reactor"}, 500

def update_reactor(reactor_id, updated_reactor_data):
    # Obtener el reactor existente por su ID
    existing_reactor = reactor_service.get_reactor_by_id(reactor_id)
    if existing_reactor:
        # Actualizar los datos del reactor existente con los nuevos datos proporcionados
        for key, value in updated_reactor_data.items():
            setattr(existing_reactor, key, value)
        # Llamar al servicio para actualizar el reactor en la base de datos
        success = reactor_service.update_reactor(existing_reactor)
        if success:
            return {"message": "Reactor actualizado exitosamente"}, 200
    return {"error": "Error al actualizar el reactor"}, 500