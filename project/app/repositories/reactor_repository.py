from project.app.context.db_connection import Session
from project.app.models.reactor import Reactor, Ubicacion, Estado, TipoReactor, Pais


class ReactorRelationalRepository:

    def __init__(self):
        self.session = Session().session

    # 1. Obtener reactores registrados
    def get_all_reactors(self):
        results = self.session.query(Reactor, Estado.estado, Ubicacion.ciudad, Pais.pais, TipoReactor.tipo).join(
            Estado, Reactor.id_estado == Estado.id, isouter=True).join(
                TipoReactor, Reactor.id_tipo_reactor == TipoReactor.id, isouter=True
            ).join(
                Ubicacion, Reactor.id_ubicacion == Ubicacion.id, isouter=True
            ).join(
                Pais, Ubicacion.id_pais == Pais.id, isouter=True
            ).all()
        response = []
        for result in results:
            reactor = self.model_as_dict(result[0])
            response.append(
                {
                    **reactor,
                    'estado': result[1],
                    'ciudad': result[2],
                    'pais': result[3],
                    'tipo': result[4]
                }
            )
        return response


    # 2. Obtener un reactor por Id
    def get_reactor_by_id(self, id: int):
        result = self.session.query(Reactor, Estado.estado, Ubicacion.ciudad, Pais.pais, TipoReactor.tipo).join(
            Estado, Reactor.id_estado == Estado.id, isouter=True).join(
                TipoReactor, Reactor.id_tipo_reactor == TipoReactor.id, isouter=True
            ).join(
                Ubicacion, Reactor.id_ubicacion == Ubicacion.id, isouter=True
            ).join(
                Pais, Ubicacion.id_pais == Pais.id, isouter=True
            ).filter(Reactor.id == id).first()
        return {
            **self.model_as_dict(result[0]),
            'estado': result[1],
            'ciudad': result[2],
            'pais': result[3],
            'tipo': result[4]
        }

    # 3. Crear un nuevo reactor

 

    def create_reactor(self, reactor: dict):

        pais = self.session.query(Pais).filter(Pais.pais == reactor['pais']).first()
        if pais is None:
            self.session.add(Pais(pais=reactor['pais']))
            self.session.commit()
        ubicacion = self.session.query(Ubicacion).filter(Ubicacion.ciudad==reactor['ciudad'], Ubicacion.id_pais == pais.id).first()
        if ubicacion is None:
            self.session.add(Ubicacion(ciudad=reactor['ciudad'], id_pais=pais.id))
            self.session.commit()
        estado = self.session.query(Estado).filter(Estado.estado == reactor['estado']).first()
        if estado is None:
            self.session.add(Estado(estado=reactor['estado']))
            self.session.commit()
        tipo = self.session.query(TipoReactor).filter(TipoReactor.tipo == reactor['tipo']).first()
        if tipo is None:
            self.session.add(TipoReactor(tipo=reactor['tipo']))
            self.session.commit()

        reactor_item = {
        'nombre': reactor['nombre'],
        "potencia_termica": reactor['potencia_termica'],
        "primera_fecha_reaccion": reactor['primera_fecha_reaccion'],
        "id_tipo_reactor": tipo.id,
        "id_ubicacion": ubicacion.id,
        "id_estado": estado.id
        }

        reactor_object = Reactor(**reactor_item)
        self.session.add(reactor_object)
        self.session.commit()

        return {'message': 'El reactor ha sido insertado con éxito'}



    # 5. Eliminar un reactor existente
    def delete_reactor_by_id(self, id: int):
        reactor = self.session.query(Reactor).filter(Reactor.id == id).first()
        self.session.delete(reactor)
        self.session.commit()
        return {'message': f'El reactor con id {id} fue eliminado con éxito'}
    
    # 6. Obtener tipos de reactores registrados
    def get_all_reactor_types(self):
        results = self.session.query(TipoReactor).all()
        response = []
        for result in results:
            response.append(self.model_as_dict(result))
        return response
    
    # 8. Obtener Ubicaciones Registradas
    def get_all_locations(self):
        results = self.session.query(Ubicacion.ciudad, Pais.pais).join(Pais, Ubicacion.id_pais == Pais.id, isouter=True).all()
        response = []
        for result in results:
            response.append(
                {
                    'ciudad': result[0],
                    'pais': result[1]
                }
            )
        return response
    

    # Funcion para transformar objeto de un modelo a diccionario 
    def model_as_dict(self, object):
        return {attr.key: getattr(object, attr.key) for attr in object.__mapper__.attrs}