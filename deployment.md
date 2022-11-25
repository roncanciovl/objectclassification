# Recomendaciones para que el código se logre ejecutar 

La instalación requiere 2 GB de memoria

Instalar git para windows (o para su OS) en caso de no tenerlo instalado
https://gitforwindows.org/

Se requiere tener instalado el interpretador de python en version mayor a 3.9.0

# Pruebas desde VS Code

Un tutorial para la instalación de VS code se encuentra en este link:
https://code.visualstudio.com/docs/python/python-tutorial


Abra un terminal (menu superior) en VS code y verifique el siguiente comando

```shell script
python --version
```
Si la respuesta fue una versión de Python mayor a 3.9.0 puede saltar a implementación. 

Si no, entonces deberá instalar una versión más reciente.

Si previamente instaló Python con anaconda, una opción es realizar un upgrade de anconda, para esto abra el Anaconda prompt y envie el siguiente comando, puede tardar mucho.

```shell script
conda install python=3.10.8
```

En caso de ningún retorno por parte de este comando, o debera instalar python https://www.python.org/downloads/release/python-3108/ o debe entonces verificar lo siguiente

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

Desde el terminal de VS code envie el siguiente comando. Despues de enviado le debe aparecer una ventana preguntando si quiere vincular este environment al workspace actual, selecciones Si.

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

Si se cierra este terminal y se abre otro nuevo, es necesario activar el environment otra vez:

```shell script
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.robotenv\Scripts\activate
```

## Por ultimo se instalan los paquetes en el environment (.robotenv)

```shell script
python -m pip install --upgrade pip
```
Si en este punto le aparece el siguiente WARNING o un error, la instalación requiere unas configuraciones adicionales. En caso contrario salte al siguiente comando.

```shell script
WARNING: pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
```
Probablemente su environment tomó una preinstalación del interpretador de Python de Anaconda o de alguna otra preninstalación, y su environment no encuentra el camino o PATH a algunas "libraries" necesarias.

La solución es agregar el PATH C:\\...\anaconda3\Library\bin a las variables de entorno del sistema operativo. Note que los ... depende de cada computador, normalmente la carpeta que necesitamos se encuentra en este camino o PATH C:\Users\username\anaconda3\Library\bin pero deberá verificarlo en su computador. 

Pasos:

1. Cierre VScode
2. Agregue este PATH a través de "Editar la variables de entorno del sistema" (busqueda de windows). No olvide al final darle aceptar a todas la ventanas. https://parzibyte.me/blog/2017/12/21/agregar-directorio-path-windows/
3. Abra de nuevo VScode
4. Habilite los permisos para activar el environment desde un terminal
5. Active el environment
6. Verifique el cambio, enviando el comando de instalación anterior: python -m pip install --upgrade pip


Siguiente comando:


```shell script
pip install -r requirements.txt
```


## Anotaciones adicionales. No son necesarias en la instalación


El archivo .gitignore se ha configurado para evitar que el environment se guarde en el repositorio. Adicionando la siguiente linea dentro en el archivo: .robotenv

En caso de instalar nuevos paquetes, se require actualizar el archivo de requerimientos de paquetes

```shell script
pip freeze > requirements.txt
```

# Como se verifica la instalación?

Ejecutar(Run) el script o archivo ai.py, despues de algunos segundos debería abrir una imagen y aparecer en el termina la categoira del objeto en la imagen, si funcionó, entonces presionar cualquier tecla para terminar la ejecución.

Cuando se ejecuta un script de python (*.py) vscode abre otro terminal, este nuevo terminal tiene el nombre de Python, aqui el environment no esta activado. Por lo que para hacer cambios en el evironment hay que cambiar de terminal o abrir uno nuevo y activar alli el environment.

# Integración con Matlab

Necesitamos saber el PATH al script de nuestro environment que llama el ejecutable de python

Para esto podemos ejecutar codigo de python desde el terminal en VScode asegurandose que nuestro environment este activo en ese terminal. Envie el comando python en el terminal para abrir una consola de python dentro del terminal.

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
            'C:\Users\username\.robotenv\Scripts\python.exe', ... 
            'ExecutionMode','OutOfProcess') 
```

Respuesta esperada o similar

```shell script
ans = 
  PythonEnvironment with properties: 
          Version: "3.9" 
       Executable: "C:\Users\username\objectclassification\.robotenv\Scripts\python.exe" 
          Library: "C:\Users\username\anaconda3\python39.dll" 
             Home: "C:\Users\username\objectclassification\.robotenv" 
           Status: NotLoaded 
    ExecutionMode: OutOfProcess
```
Verifique que las bibliotecas se cargaron con el siguiente comando en MATLAB

```shell script
>> py.importlib.import_module('cv2')
```
Si no hay error y hay alguna answer (ans=), este modulo ya esta listos para usar.

IMPORTANTE: El comando anterior requiere ingresar el nombre de modulo de python, este nombre de modulo es el nombre que aparece al inicio de los archivos de python (*.py) 

```shell script
import <nombre_del_modulo>
```
Debera importar todos los modulos de python que requiere un Script de python (*.py) para que le Script funcione


REf: https://www.mathworks.com/matlabcentral/answers/1750425-python-virtual-environments-with-python-interface

# Recomendaciones importantes para usar este repositorio de GitHub

Si su intención es usar todo el código para su proyecto, la recomendación es crear un "branch" nuevo a partir del branch del master (tambien llamado main). Desde el terminal envie el siguiente comando. Como sugerencia new-branch-name puede ser el nombre de su robot  

```shell script
git checkout -b ＜new-branch-name＞
```
A partir de aquí ya puede realizar cambios en el código.

## Cómo actualizar el código si hay un nuevo release en el repositorio de Github

Primero se recomienda realizar un "commit" en su branch, antes de cualquier actualización. [Saving changes on git](https://www.atlassian.com/git/tutorials/saving-changes)

Desde el terminal de vs code, envie el siguiente comando. Asegurese que el PATH del terminal esta en la carpeta del proyecto. 

```shell script
git checkout main
```

```shell script
git pull
```
Esto primero actualiazrá sus archivos en el computador (tambien llamado local) en el branch principal (main o master) con los archivos del respositorio (tambien llamado remote) 

Luego el siguiente comando fusionará las ultimas actualizaciones que ya están en su computador (en el branch principal) con el código del branch de su robot ＜your-branch-name＞. Aqui puden aparecer conflictos que tendrá que revisar archivo por archivo. 


```shell script
git checkout ＜your-branch-name＞
```
```shell script
git merge main
```
Si algo salió mal con el merge y quiere devolverse al estado anterior envie el siguiente comando (solo funciona si realizó un commit antes de la actualización):

```shell script
git reset --hard HEAD~1
```
## Otros

Would you like Code to periodically run 'git fetch'? No

# VS code no funciona de acuerdo a lo esperado

Ctrl+Shift+P -> Reload Window

