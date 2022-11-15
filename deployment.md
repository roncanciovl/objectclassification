# Información para que funcione el código 

La instalación requiere 2 GB de memoria

Se requiere tener instalado el interpretador de python 3.9.x

# Pruebas desde VS Code

https://code.visualstudio.com/docs/python/python-tutorial


Abra un terminal en VS code y verifique el siguiente comando

```shell script
python --version
```
Si la respuesta fue Python 3.9.x puede saltar a implementación, si no verificar lo siguiente

1. Verifique que el interpretador de python esta instalado, si esta instalado entonces
2. Primero abrir un terminal del sistema operativo y probar el comando anterior, si no funciona
3. debera agregar el PATH del archivo python.exe a las variables de entorno del sistema


# Implementación en VS Code

## Clonar el repositorio

Desde VS code presionar ctrl+shift+p y escribir Git:Clone, enter para seleccionar

En nombre del repositorio coloque

```shell script
https://github.com/roncanciovl/objectclassification
```
Luego seleccione una carpeta en su computador donde pueda disponer de los 2GB que require la instalación

Abrir en una ventana o ventana nueva si ya hay abierto algún proyecto en su VS code, no lo agregue a su actual workspace

Despues de esto VS Code crea automaticamente un workspace para este proyecto donde se puede agregar un enviroment 


## La recomendación es entonces crear un environment

Desde el terminal de VS code

```shell script
python -m venv .robotenv
```

## Luego se debera activar el environment para instalar los paquetes

```shell script
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.robotenv\Scripts\activate
```
## Por ultimo se instalan los paquetes en el environment (.robotenv)

```shell script
python -m pip install --upgrade pip
pip install -r requirements.txt
```






Si se cierra este terminal y se abre otro nuevo, es necesario activar el environment otra vez:

```shell script
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.robotenv\Scripts\activate
```



El archivo .gitignore se ha configurado para evitar que el environment se guarde en el repositorio

Adicionando la siguiente linea dentro en el archivo

.robotenv


En caso de instalar nuevos paquetes, se require actualizar el archivo de requerimientos de paquetes

```shell script
pip freeze > requirements.txt
```

# Como se verifica la instalación?

Ejecutar(Run) el scrip o archivo ai.py, despues de alguno segundos debería abrir una imagen de una botella, si funciono, entonces oprimir cualquier tecla para terminar la ejecución 
