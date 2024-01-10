# Práctica Gestor Personal - Estructura y Modelos

En esta práctica, desarrollaremos una herramienta de gestión personal que constará de dos funciones principales: la gestión de contactos y la organización de tareas.

## Funcionalidades

### Gestión de Contactos
1. Agregar Contacto: Añadir nuevos contactos a la agenda personal.

2. Editar Contacto: Modificar la información de un contacto existente.

3. Eliminar Contacto: Eliminar contactos de la agenda.

4. Listar Contactos: Mostrar la lista completa de contactos almacenados.

5. Búsqueda de Contactos: Buscar contactos específicos en la agenda.

### Organización de Tareas
1. Agregar Tarea: Incluir nuevas tareas en la lista.

2. Editar Tarea: Modificar la información de una tarea existente.

3. Eliminar Tarea: Eliminar tareas de la lista.

4. Otras Funciones de Organización: Capacidades adicionales para organizar y gestionar eficientemente las tareas diarias.

## Puesta en Marcha con Django

Sigue estos pasos para poner en marcha la práctica utilizando Django:

1. **Clonar el Repositorio:**
   ```bash
        git clone https://github.com/Dextron03/gestor-personal-django.git
   ```

2. **Crea un entorno virtual:**
    ```bash
        virtualenv -p python env
    ```

3. **Instalar Dependencias:**
    ```bash
        pip install -r requirements.txt
    ```
4. **python manage.py migrate:**
    ```bash
        python manage.py makemigrations
        python manage.py migrate
    ```
5. **Crear un Superusuario (para administrar el sitio):**
    ```bash
        python manage.py createsuperuser
    ```
6. **Ejecutar el Servidor de Desarrollo:**
    ```bash
        python manage.py runserver
    ```
