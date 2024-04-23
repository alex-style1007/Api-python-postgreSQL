from pydantic import BaseModel
from typing import Union
from datetime import datetime

class ReactorResponseModel(BaseModel):
    id:                         int
    nombre:                     str
    potencia_termica:           str
    primera_fecha_reaccion:     Union[datetime, None]
    tipo:                       str
    estado:                     str
    ciudad:                     str
    pais:                       str



class ClientModel(BaseModel):
    id:          int
    nombre:      str
    apellido:    str
    producto:    str
    ciudad:      str
    correo:      Union[str, None]