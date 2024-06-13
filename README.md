## Clonar y Ejecutar una Aplicación Django Localmente

1. **Clonar el proyecto desde GitHub**:
   - Abre una terminal o línea de comandos.
   - Navega a la ubicación donde deseas guardar el proyecto.
   - Ejecuta el siguiente comando para clonar el repositorio:
     ```
     git clone https://github.com/edwinfigueroa15/alto-server
     ```


2. **Configurar un entorno virtual**:
   - Crea un entorno virtual para aislar las dependencias del proyecto:
     ```
     python -m venv venv
     ```
   - Activa el entorno virtual:
     - En Windows: `venv\Scripts\activate`
     - En Linux/macOS: `source venv/bin/activate`

3. **Instalar las dependencias**:
   - Navega al directorio del proyecto clonado:
     ```
     cd nombre_del_proyecto
     ```
   - Instala las dependencias especificadas en el archivo `requirements.txt`:
     ```
     pip install -r requirements.txt
     ```

4. **Configurar la base de datos**:
   - Crea una base de datos local en este caso se uso `PostgreSQL` y si ya lo tienes instalado ejecuta el comando:
     ```
     python manage.py migrate
     ```

5. **Ejecutar el proyecto**:
   - Inicia el servidor de desarrollo:
     ```
     python manage.py runserver
     ```
   - Abre tu navegador y ve a `http://127.0.0.1:8000/api/v1/` para ver la aplicación.
