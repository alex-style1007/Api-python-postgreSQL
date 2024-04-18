from context.db_connection import connect_to_database
from model.reactor import Reactor

class ReactorRepository:
    def __init__(self):
        self.connection=connect_to_database()
    #CONSULTAR TODOS LOS REACTORES
    def get_all_reactores(self):
        try:
            cursor=self.connection.cursor()
            cursor.execute("""
                           SELECT * FROM reactores
                           """)
            reactors_data=cursor.fetchall()
            reactors=[Reactor(*data) for data in reactors_data]
            return reactors
        except Exception as e:
            print("Error consultando todos los reactores",e)
            return None
    #CRUD PARA CREAR UN REACTOR   
    def create_reactor(self,reactor):
        try:
            cursor=self.connection.cursor()
            cursor.execute("""
                           INSERT INTO reactores(nombre_reactor,tipo_reactor,potencia_termica,estado_reactor,fecha_primera_reaccion,ciudad,pais_id)
                           VALUES (%s,%s,%s,%s,%s,%s,%s)
                           RETURNING reactor_id
                           """,(reactor.nombre_reactor,reactor.tipo_reactor,reactor.potencia_termica,reactor.estado_reactor,reactor.fecha_primera_reaccion,reactor.ciudad,reactor.pais_id))
            reactor_id=cursor.fetchone()[0]
            self.connection.commit()
            return reactor_id
        except Exception as e:
            print ("Error creando el reactor:",e)
            self.connection.rollback()
            return None
    #CRUD PARA CONSULTAR UN REACTOR POR ID   
    def reactor_by_id(self,reactor_id):
        try:
            cursor=self.connection.cursor()
            cursor.execute("""
                           SELECT * FROM reactores WHERE reactor_id = %s""",(reactor_id))
            reactor_data=cursor.fetchone()
            if reactor_data:
                return Reactor(*reactor_data)
            else:
                return None
        except Exception as e:
            print("Error consultando la informacion de el reactor con id:",e)
            return None
    #CRUD PARA TRAER TODOS LOS TIPOS DE REACTORES REGISTRADOS   
    def get_all_types_reactor(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT DISTINCT tipo_reactor FROM reactores
            """)
            types_data = cursor.fetchall()
            types = [row[0] for row in types_data]
            return types
        except Exception as e:
            print("Error fetching all reactor types:", e)
            return None
    
    #consultar el tipo por id y traer todos los reactores asociados a ese tipo
    def get_reactors_by_type_id(self, reactor_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT r.nombre_reactor, r.tipo_reactor, r.potencia_termica, r.estado_reactor, r.fecha_primera_reaccion, r.ciudad, r.pais_id
                FROM reactores r
                JOIN reactores rt ON r.tipo_reactor = rt.tipo_reactor
                WHERE r.reactor_id = %s
            """, (reactor_id,))
            reactor_data = cursor.fetchone()
            if reactor_data:
                # El primer elemento es el nombre del reactor
                nombre_reactor = reactor_data[0]
                # El segundo elemento es el tipo de reactor asociado al reactor dado
                tipo_reactor = reactor_data[1]
                # Los elementos restantes son los datos del reactor
                reactor_info = reactor_data[2:]
                # Crear el objeto Reactor con los datos obtenidos
                reactor = Reactor(reactor_id, nombre_reactor, tipo_reactor, *reactor_info)
                return reactor
            else:
                return None
        except Exception as e:
            print("Error estrayendo todos los reaactores asociado al tipo del reactor_ID:", e)
            return None      
    
    #Eliminar un reactor existente
    def delete_reactor(self,reactor_id):
        try:
            cursor=self.connection.cursor()
            cursor.execute("""
                           DELETE FROM reactores WHERE reactor_id = %s"""
                           ,(reactor_id))
            self.connection.commit()
            return True
        except Exception as e:
            print("Error eliminando reactor:",e)
            self.connection.rollback()
            return False