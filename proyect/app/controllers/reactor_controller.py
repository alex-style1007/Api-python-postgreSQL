from typing import List
from fastapi import FastAPI, status, Path, Query, Body, Depends
from models.reactor_schema import ReactorResponseModel, TypeReactorModel, LocationReactorModel
from services.reactor_service import ReactorService
from utils.utils import get_session


app = FastAPI()

# 1. Obtener reactores registrados.
@app.get(
        path='/reactors',
        status_code=status.HTTP_200_OK,
        response_model=List[ReactorResponseModel],
)
async def get_reactors(session = Depends(get_session)):
    return ReactorService().get_all_reactors()

# 2. Obtener un reactor por Id.
@app.get(
        path='/reactors/{id}',
        status_code=status.HTTP_200_OK,
        response_model=List[ReactorResponseModel],
)
async def get_reactors(session = Depends(get_session), id: int = Path(...)):
    return ReactorService().get_reactor_by_id(id)

# 3. Crear un nuevo reactor.
@app.post(
        path='/reactors',
        status_code=status.HTTP_200_OK,
)
async def get_reactors_by_id(session = Depends(get_session), reactor: ReactorResponseModel=Body(...)):
    return ReactorService().create_reactor(reactor.model_dump())

# 4. Actualizar un reactor existente.
@app.put(
        path='/reactors',
        status_code=status.HTTP_200_OK,
)
async def get_reactors_by_id(session = Depends(get_session), reactor: ReactorResponseModel=Body(...)):
    return ReactorService().update_reactor(reactor.model_dump())

# 5. Eliminar un reactor existente.
@app.delete(
        path='/reactors/{id}',
        status_code=status.HTTP_200_OK,
)
async def get_reactors_by_id(session = Depends(get_session), id: int=Path(...)):
    return ReactorService().delete_reactor(id)

# 6. Obtener tipos de reactores registrados.
@app.get(
        path='/reactors/types',
        status_code=status.HTTP_200_OK,
        response_model=List[TypeReactorModel],
)
async def get_reactors(session = Depends(get_session)):
    return ReactorService().get_all_types_reactor()

# 7. Obtener tipo de reactor por Id. Respuesta incluye todos los reactores asociados al tipo.
@app.get(
        path='/reactors/types/{id}',
        status_code=status.HTTP_200_OK,
        response_model=List[TypeReactorModel],
)
async def get_reactors(session = Depends(get_session), id: int = Path(...)):
    return ReactorService().get_reactors_by_type_id(id)

# 8. Obtener Ubicaciones Registradas.
@app.get(
        path='/reactors/locations',
        status_code=status.HTTP_200_OK,
        response_model=List[LocationReactorModel],
)
async def get_reactors(session = Depends(get_session)):
    return ReactorService().get_all_locations()

# 9. Obtener Ubicación por Id.
@app.get(
        path='/reactors/locations/{id}',
        status_code=status.HTTP_200_OK,
        response_model=List[LocationReactorModel],
)
async def get_reactors(session = Depends(get_session), id: int = Path(...)):
    return ReactorService().get_locations_by_id(id)

# 10. Obtener Reactores registrados por Ubicación
@app.get(
        path='/reactors/locations/{id}',
        status_code=status.HTTP_200_OK,
        response_model=List[LocationReactorModel],
)
async def get_reactors(session = Depends(get_session), id: int = Path(...)):
    return ReactorService().get_locations_by_id(id)



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