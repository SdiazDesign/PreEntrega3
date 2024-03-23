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

El Proyecto cuenta con las urls para ver, cargar, editar y eliminar 4 tipos de entidades:

- Equipos
- Partidos
- Resultados
- Posiciones

Además de las urls para el manejo de sesiones y mantenimiento de cuenta de usuario.

Cada una de ellas es accesible desde el menú del navbar. Y en el footer, tenemos el enlace "Acerca de mí" que dispone de una página más con información personal.

## Acceso a admin

Super Usuario solicitado:
- Usuario: coderhouse
- Pass: coderhouse

Acceso: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Video Explicativo
https://drive.google.com/file/d/1-EkwZPV4nK8sHhpoiYN90GJ5NThjmgkV/view?usp=sharing
