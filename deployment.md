Desde el terminal de VS code 

La instalación requiere 1GB de memoria

Se requiere tener instalado el interpretador de python 3.9.x
Desde VScode presionar Ctrl+Shift+P, luego escribir Pyyhon: Select Interpreter, y seleccionar Python 3.9.x

(Si windows no detecta el comando "python" debera agregar el PATH del archivo python.exe a las variables de entorno de windows)


Comandos :

python -m venv .robotenv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.robotenv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt


Si se cierra este terminal y se abre otro nuevo, es necesario activar el environment otra vez:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
robotenv\Scripts\activate


Configurar .gitignore para evitar que el environment se guarde en el repositorio

Adicionando la siguiente linea

.robotenv