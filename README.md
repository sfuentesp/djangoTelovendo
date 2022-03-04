## Nombre del proyecto
  Telovendo
## Descripción
  Tienda de ventas online de productos para mascotas
## Autores
  Simón Fuentes
  Matias Muñoz
  Allison Ossa
  Angelo Valenzuela


## Instalación
Debe instalar python 3.9
una ves instalado python debe iniciar un entorno virtual para poder instalar las dependencias necesarias,
puede instalar los componentes desde el archivo requirements.txt o ejecutar el comando pip install "nombre de app"
asgiref==3.5.0
Django==4.0.2
django-crispy-forms==1.14.0
gunicorn==20.1.0
Pillow==9.0.1
psycopg2==2.9.3
sqlparse==0.4.2

El sistema trabaja con un motor de base de datos postgresql por ende debe instalar aquel motor de base de datos

despues en el settigns.py debes moficar el nombre de usuario y password en en la parte de base de datos por los valore que dejaste al momento de instalar postgresql

Por ultimos debes ejecutar el comando de python manage.py migrate para generar las tablas en el motor segun los modelos 
que estan creados en el proyecto
