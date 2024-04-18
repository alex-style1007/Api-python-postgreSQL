import os
import psycopg2

def connect_to_database():
    try:
        # Obtener las variables de entorno
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT')
        db_name = os.getenv('DB_NAME')
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        
        # Establecer la conexión a la base de datos
        connection = psycopg2.connect(
            host=db_host,
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_password
        )

        print("Conexión exitosa a la base de datos.")
        return connection

    except (Exception, psycopg2.Error) as error:
        print("Error al conectar a la base de datos:", error)
        return None
