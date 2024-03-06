## Proyecto
Proyecto Demo para la pre entrega 3 del curso de CoderHouse sobre Python
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

## Urls
El Proyecto cuenta con las siguients url.

- http://127.0.0.1:8000/App/
- http://127.0.0.1:8000/App/crear_equipo/
- http://127.0.0.1:8000/App/crear_partido/
- http://127.0.0.1:8000/App/crear_resultado/
- http://127.0.0.1:8000/App/get_resultado/
- http://127.0.0.1:8000/App/buscar_resultado/

Igualmente, cada una de ellas es accesible desde el menu del navbar. 
