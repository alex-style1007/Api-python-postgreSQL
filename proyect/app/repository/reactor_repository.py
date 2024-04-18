from context.db_connection import connect_to_database
from model.reactor import Reactor

class ReactorRepository:
    def __init__(self):
        self.connection=connect_to_database()
        
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
    