# test_houm

## Instalación

   - Puedes clonar el repositorio en la carpeta que desees con el comando:

```
$ git clone url
```


   - Luego de clonado el repositorio puedes abrir la carpeta en VS Code o en el compilador que desees.

## Ejecución

   - Creas una nueva terminar dirigientote a Terminal > New terminal.
   - Luego te diriges a la terminal creada y procedemos a instalar los requerimientos del archivo requirements.txt.
   
```
$ pip install -r requirements.txt
```
   - Una vez intalado los requirements, realizar la ejecución del archivo console.py con el siguiente comando:
  
 ```
$ python3 console.py
```
Una vez allí se desplegará un menú de opciones con el cual vas a poder interacturar para probar las diferentes funcionalidades del programa.


## Consideraciones
El programa fue realizado con una versión de Python
```
Python 3.7.9
```
Además se le aplicó black al codigo para su organización, acompañado de algunas consideraciones de estilo PEP 8.

#### Nota:
Se consideró impementar métodos asincrónicos con httpx, sin embargo, al ver la cantidad de solicitudes que podian llegar a hacer dentro de algún for, considere que no era tan necesario, pues el volumen de solicitudes al API no era un gran número. 

De esta misma manera sucede con el multiprocesamiento con Process, pues no fue necesario debido al volumen de llamados.
