# Información para que funcione el código 

La instalación requiere 2 GB de memoria

Instalar git para windows (o para su OS) en caso de no tenerlo instalado
https://gitforwindows.org/

Se requiere tener instalado el interpretador de python en version mayor a 3.9.0

# Pruebas desde VS Code

Asgurarse de instalar la extensión de python para VS Code 
https://code.visualstudio.com/docs/python/python-tutorial


Abra un terminal en VS code y verifique el siguiente comando

```shell script
python --version
```
Si la respuesta fue una versión de Python mayor a 3.9.0 puede saltar a implementación, si no entonces instalar una versión más reciente. En caso de ningún retorno por parte de este comando, entonces verificar lo siguiente

1. Verifique que el interpretador de python está instalado, si está instalado entonces
2. Primero abrir un terminal del sistema operativo y probar el comando anterior, si no funciona
3. debera agregar el PATH del archivo python.exe a las variables de entorno del sistema


# Implementación en VS Code

## Clonar el repositorio

Desde VS code presionar ctrl+shift+p y escribir Git:Clone, enter para seleccionar

En nombre del repositorio coloque

```shell script
https://github.com/roncanciovl/objectclassification
```
Luego seleccione una carpeta en su computador en el directorio de su usuario(username) de windows C:\users\username, donde pueda disponer de los 2GB que require la instalación

VS code le pedirá abrir una ventana de VS code, o puede escoger una ventana nueva si ya hay abierto algún proyecto en su VS code, no lo agregue a su actual workspace

Despues de esto VS Code crea automaticamente un workspace para este proyecto donde se puede agregar un enviroment 


## La recomendación es entonces crear un environment

Desde el terminal de VS code. Le debe aparecer una ventana preguntando si quiere vincular este enviroment al workspace actual, selecciones Si.

```shell script
python -m venv .robotenv
```

Al crear el environment se crea una carpeta .robotenv dentro del workspace con algunos Scripts, entre ellos se crea un link al ejecutable de python del sistema operativo: .robotenv\Scripts\python.exe. En esa carpeta tambien se guardaran las bibliotecas (libraries) necesarias para el proyecto.

## Luego se debera activar el environment para instalar los paquetes

Envie primero este comando para habilitar permisos, toda la linea es el comando

```shell script
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
Comando para activar el environment:

```shell script
.robotenv\Scripts\activate
```
Luego de activarlo deberá aparecer al lado izquierdo entre parentesis el nombre del environment activo. 

```shell script
(.robotenv) C:\Users\username\
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

Ejecutar(Run) el script o archivo ai.py, despues de algunos segundos debería abrir una imagen, si funcionó, entonces presionar cualquier tecla para terminar la ejecución.

Cuando se ejecuta un script de python (*.py) vscode abre otro terminal, este nuevo terminal tiene el nombre de Python, aqui el environment no esta activado. Por lo que para hacer cambios en el evironment hay que cambiar de terminal o abrir uno nuevo y activar alli el environment.

# Integración con Matlab

Necesitamos saber el PATH al script de nuestro environment que llama el ejecutable de python

Para esto podemos ejecutar codigo de python desde el terminal. Envie el comando python en el terminal para abrir una consola de python dentro del terminal.

```shell script
python
```
Luego escriba las siguiente lineas de código

```shell script
(.robotenv) C:\Users\username$ python 
>>> import sys 
>>> sys.executable 
```
Algo como esto debe aparecer, copielo

C:\Users\username\ .robotenv\Scripts\python.exe

Para salir de la consola de python envie el siguiente comando
```shell script
>>> exit()
```


Abra una ventana de comandos de MATLAB y envie esta configuración cambiando el PATH de acuerdo al paso anterior. 

```shell script
>> pyenv('Version', ... 
            'C:\Users\username\.robotenv\Scripts\python', ... 
            'ExecutionMode','OutOfProcess') 
```

Respuesta esperada o similar

```shell script
ans = 
  PythonEnvironment with properties: 
          Version: "3.8" 
       Executable: "C:\Users\username\.robotenv\Scripts\python.EXE" 
          Library: "C:\Users\gmkep\AppData\Local\Programs\Python\Python38\python38.dll" 
             Home: "C:\Users\username\py38" 
           Status: NotLoaded 
    ExecutionMode: OutOfProcess
```
Verifique que las bibliotecas se cargaron con el siguiente comando en MATLAB

```shell script
>> py.importlib.import_module('tensorflow-cpu')
```
REf: https://www.mathworks.com/matlabcentral/answers/1750425-python-virtual-environments-with-python-interface

# Cómo actualizar el código si hay un nuevo release en el repositorio de Github

Desde el terminal de vs code, envie el siguiente comando. Probablemente require instalar GIT. 

```shell script
git pull
```

