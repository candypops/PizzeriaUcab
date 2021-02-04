# PizzeriaUcab

Aplicación desarrollada en Django para la toma de pedidos de pizza y reportes de los mismos.


## Requisitos
* Python 3 o superior
* Ambiente virtual
* Django 3.1 o superior

## Instrucciones para su uso
* Descargue el proyecto
* Ubíquese en la carpeta del proyecto 
* Ingrese a su ambiente virtual 
  * Linux o MacOS:  ``` $source venv/bin/activate ```
  * Para Windows: ```  $ venv\Scripts\activate.bat ```

* Ejecute los siguientes comandos para la base de datos
  * ```  python manage.py makemigrations ```
  * ```  python manage.py migrate ```
  
* Para ejecutar el proyecto realice el siguiente comando
```python manage.py runserver```

* En caso de ser necesario puede crear un super usuario y acceder al administrador de django de la siguiente manera
  * ```python manage.py createsuperuser```
  * Una vez culminado, realizar el paso anterior para ejecutar el proyecto e ir a la ruta */admindjango*

En caso de que haya un error con los archivos estáticos, ejecutar:

```  python manage.py collectstatic```


## Autores
#### Equipo 4:
* María Avendaño
* Miguel Coccaro
* Ovidio Rodriguez
