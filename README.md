## Proyecto
Proyecto Demo para el proyecto Final del curso de CoderHouse sobre Python
El proyecto, con su respectiva App, simula la carga de equipos, partidos y resultados para un torneo de Futbol

## Installation
Necesita tener instalado Python 3.10.0 y pip-
Luego, instalar django
```bash
python -m pip install Django
```

Una vez lenvantado el entorno, se debe correr las migraciones con los siguientes comandos:
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

## Urls
El Proyecto cuenta con las urls para ver, cargar, editar y eliminar 4 tipo de entidades 
  equipos
  partidos
  resultados
  posiciones

Ademas de las urls para el manejo de sesion y mantenimiento de cuenta de usuario. 

Cada una de ellas es accesible desde el menu del navbar. Y en el footer, tenemos el enlace Acerca de mi que dispone de una pagina mas con informacion personal 
