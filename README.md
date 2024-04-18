# tadb_202410_ex03
# Estructura de Carpetas de un Proyecto Flask

- **app/**
  - **Controller/**: Contiene los controladores de la aplicación Flask, que manejan las rutas y las solicitudes HTTP.
  - **model/**: Contiene las definiciones de los modelos de datos de la aplicación.
  - **repository/**: Contiene los repositorios que interactúan con la base de datos.
  - **service/**: Contiene los servicios que implementan la lógica de negocio de la aplicación.
  - **context.py**: Define la configuración y la gestión del contexto de la aplicación, incluida la conexión a la base de datos.
  - **main.py** (o **app.py**): Punto de entrada principal de la aplicación Flask, donde se crea la instancia de la aplicación y se configuran las rutas.
  - **config.py**: Archivo de configuración de la aplicación, que define variables de configuración como las claves secretas, las configuraciones de la base de datos, etc.

- **static/**: Directorio opcional que contiene archivos estáticos como CSS, JavaScript, imágenes, etc.

- **README.md**: Archivo de documentación que proporciona información sobre el proyecto, cómo configurarlo, ejecutarlo y usarlo.

- **.gitignore**: Archivo que especifica qué archivos y directorios deben ser ignorados por Git durante el versionado del proyecto.

- **.env**: Archivo que contiene variables de entorno para la configuración local del proyecto, como claves secretas, configuraciones de la base de datos, etc.
