from typing import List
from fastapi import FastAPI, status, Path, Query, Body, Depends
from project.app.models.reactor_schema import ReactorResponseModel, ReactorTypeResponseModel, LocationResponseModel
from project.app.services.reactor_service import ReactorService

app = FastAPI()

# 1. Obtener reactores registrados.
@app.get(
        path='/reactors',
        status_code=status.HTTP_200_OK,
        response_model=List[ReactorResponseModel],
)
async def get_reactors():
    return ReactorService().get_all_reactors()

# 6. Obtener tipos de reactores registrados.
@app.get(
        path='/reactors/types',
        status_code=status.HTTP_200_OK,
        response_model=List[ReactorTypeResponseModel],
)
async def get_all_reactor_types():
    return ReactorService().get_all_reactor_types()

# 8. Obtener Ubicaciones Registradas.
@app.get(
        path='/reactors/locations',
        status_code=status.HTTP_200_OK,
        response_model=List[LocationResponseModel],
)
async def get_all_locations():
    return ReactorService().get_all_locations()

# 2. Obtener un reactor por Id.
@app.get(
        path='/reactors/{id}',
        status_code=status.HTTP_200_OK,
        response_model=List[ReactorResponseModel],
)
async def get_reactor_by_id(id: int = Path(...)):
    return ReactorService().get_reactor_by_id(id)

# 3. Crear un nuevo reactor.
@app.post(
        path='/reactors',
        status_code=status.HTTP_201_CREATED,
)
async def create_reactor(reactor: ReactorResponseModel=Body(...)):
    return ReactorService().create_reactor(reactor.model_dump())

# 4. Actualizar un reactor existente.
@app.put(
        path='/reactors',
        status_code=status.HTTP_200_OK,
)
async def update_reactor(reactor: ReactorResponseModel=Body(...)):
    return ReactorService().update_reactor(reactor.model_dump())

# 5. Eliminar un reactor existente.
@app.delete(
        path='/reactors/{id}',
        status_code=status.HTTP_200_OK,
)
async def delete_reactor_by_id(id: int=Path(...)):
    return ReactorService().delete_reactor_by_id(id)

# 7. Obtener tipo de reactor por Id. Respuesta incluye todos los reactores asociados al tipo.
@app.get(
        path='/reactors/types/{id}',
        status_code=status.HTTP_200_OK,
        response_model=List[ReactorTypeResponseModel],
)
async def get_reactors_by_type_id(id: int = Path(...)):
    return ReactorService().get_reactors_by_type_id(id)

# 9. Obtener Ubicación por Id.
@app.get(
        path='/reactors/locations/{id}',
        status_code=status.HTTP_200_OK,
        response_model=List[LocationResponseModel],
)
async def get_locations_by_id(id: int = Path(...)):
    return ReactorService().get_locations_by_id(id)

# 10. Obtener Reactores registrados por Ubicación
@app.get(
        path='/reactors/location',
        status_code=status.HTTP_200_OK,
        response_model=List[LocationResponseModel],
)
async def get_reactor_by_location(country: str = Query(default=None), city: str = Query(default=None)):
    return ReactorService().get_reactor_by_location()
