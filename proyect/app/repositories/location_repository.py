from context.db_connection import connect_to_database

class LocationRepository:
    def __init__(self):
        self.connection=connect_to_database
    
    #Extraer todos los paises registrados
    def get_all_countries(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT * FROM paises
            """)
            countries_data = cursor.fetchall()
            countries = [{'id_pais': row[0], 'nombre_pais': row[1]} for row in countries_data]
            return countries
        except Exception as e:
            print("Error consultando las ubicaciones:", e)
            return None
    
    #obtener informacion de la ubicacion por pais
    def get_country_by_id(self, country_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT * FROM Paises WHERE id_pais = %s
            """, (country_id,))
            country_data = cursor.fetchone()
            if country_data:
                country = {'id_pais': country_data[0], 'nombre_pais': country_data[1]}
                return country
            else:
                return None
        except Exception as e:
            print("Error consultando pais por ID:", e)
            return None
    
    #Consultar los reactores disponibles en un pais
    def get_reactors_by_country_id(self, country_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT * FROM Reactores WHERE pais_id = %s
            """, (country_id,))
            reactors_data = cursor.fetchall()
            reactors = [{'reactor_id': row[0], 'nombre_reactor': row[1], 'tipo_reactor': row[2], 'potencia_termica': row[3], 'estado_reactor': row[4], 'fecha_primera_reaccion': row[5], 'ciudad': row[6], 'pais_id': row[7]} for row in reactors_data]
            return reactors
        except Exception as e:
            print("Error consultando los reactores en el pais con ID:", e)
            return None