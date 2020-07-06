# Tarea 4

## 1. Prerrequisitos

1. En carpeta raiz del proyecto, se debe crear una carpeta llamada **reports** y otra llamada **models**.
2. Crear un ambiente que tenga instalado python 3.
3. Instalar los paquetes de python que se encuentran en el archivo *requirements.txt*

## 2. Instrucciones

1. Para ejecutar el entreno del modelo, utilizar el comando `make train`. A este comando se le puede agregar el parámetro `bigram`, el cual puede ser `True` o `False` (Si dicho parámetro no se especifica, se asume `True` por defecto). Dicho comando guardará el modelo en la carpeta **models** creada en los prerrequisitos.

2. Para ejecutar el entreno del modelo y crear una visualización de este con los datos, utilizar el comando `make visualization`. A este comando se le puede agregar el parámetro `bigram`, el cual puede ser `True` o `False` (Si dicho parámetro no se especifica, se asume `True` por defecto). Dicho comando guardará una visualización del modelo con los datos en la carpeta **reports** creada en los prerrequisitos.

3. Para realizar una predicción con el modelo entrenado, utilizar el comando `make predict`. A este comando se le puede agregar el parámetro `frase`, el cual es el review al que se le quiere asignar un tema basado en el modelo. La respuesta del comando será el número de tema al que pertenece.
