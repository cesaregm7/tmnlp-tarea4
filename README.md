# Tarea 4

## 1. Prerrequisitos

1. En carpeta raiz del proyecto, se debe crear una carpeta llamada **reports** y otra llamada **models**.
2. Crear un ambiente que tenga instalado python 3.
3. Instalar los paquetes de python que se encuentran en el archivo *requirements.txt*

## 2. Instrucciones

1. Para ejecutar el entreno del modelo, utilizar el comando `make train`. A este comando se le puede agregar el parámetro `bigram`, el cual puede ser `True` o `False` (Si dicho parámetro no se especifica, se asume `True` por defecto). Dicho comando guardará el modelo en la carpeta **models** creada en los prerrequisitos.

2. Para ejecutar el entreno del modelo y crear una visualización de este con los datos, utilizar el comando `make visualization`. A este comando se le puede agregar el parámetro `bigram`, el cual puede ser `True` o `False` (Si dicho parámetro no se especifica, se asume `True` por defecto). Dicho comando guardará una visualización del modelo con los datos en la carpeta **reports** creada en los prerrequisitos.

3. Para realizar una predicción con el modelo entrenado, utilizar el comando `make predict`. A este comando se le puede agregar el parámetro `frase`, el cual es el review al que se le quiere asignar un tema basado en el modelo (Si dicho parámetro no se especifica, se coloca la frase "hotel hotel hotel" por defecto). La respuesta del comando será el número de tema al que pertenece. Además
, se le puede agregar el parámetro `bigram`, el cual puede ser `True` o `False` (Si dicho parámetro no se especifica, se asume `True` por defecto).

## 3. Resultados obtenidos con 10 topics

A continuación, se presentan los topics obtenidos del modelo cuando el número de estos se establece en 10:

0. Para este topic, las palabras más relevantes son: `book`, `say`, `check`, `ask`, `arrive`, `pay`, `leave`, `hour`, `charge` y `tell`. La interpretación que le doy a este topic es que relaciona (principalmente) los reviews respecto a la experiencia de reservación de habitaciones en el hotel y cómo fue el check in y check out de éste.

1. Para este topic, las palabras más relevantes son: `bed`, `bathroom`, `water`, `coffee`, `shower`, `free`, `think`, `big`, `light` y `modern`. La interpretación que le doy a este topic es que relaciona (principalmente) los reviews respecto a los cuartos del hotel.

2. Para este topic, las palabras más relevantes son: `little`, `have`, `romantic`, `especially`, `detail`, `wife`, `favorite`, `cost`, `exceptional` y `spot`. La interpretación que le doy a este topic es que relaciona (principalmente) los reviews respecto a los detalles y/o aspectos más positivos en la experiencia que tuvieron en el hotel.

3. Para este topic, las palabras más relevantes son: `stay`, `place`, `time`, `make`, `go`, `day`, `really`, `feel`, `amazing` y `spot`. La interpretación que le doy a este topic es que relaciona (principalmente) los reviews respecto a los lugares que visitaron durante la estadia.

4. Para este topic, las palabras más relevantes son: `cheap`, `simply`, `corner`, `guide`, `chocolate`, `desk`, `wine`, `will`, `single` y `bird`. La interpretación que le doy a este topic es que relaciona (principalmente) los reviews respecto a las actividades que podían hacer en las cercanias del hotel.

5. Para este topic, las palabras más relevantes son: `trip`, `year`, `help`, `world`, `late`, `treat`, `stunning`, `manager`, `step` y `airport`. La interpretación que le doy a este topic es que relaciona (principalmente) los reviews respecto a cómo influyó su visita al hotel respecto al viaje que realizaron.

6. Para este topic, las palabras más relevantes son: `huge`, `husband`, `choice`, `easy`, `entire`, `charm`, `order`, `ambiance`, `fine` y `add`. La interpretación que le doy a este topic es que relaciona (principalmente) los reviews respecto a cómo era el ambiente del hotel.

7. Para este topic, las palabras más relevantes son: `hotel`, `beautiful`, `service`, `restaurant`, `ground`, `visit`, `food`, `excellent`, `wonderful` y `lovely`. La interpretación que le doy a este topic es que relaciona (principalmente) los reviews respecto a las comodidades que brindaba el hotel.

8. Para este topic, las palabras más relevantes son: `room`, `staff`, `good`, `great`, `night`, `breakfast`, `nice`, `well`, `would` y `also`. La interpretación que le doy a este topic es que relaciona (principalmente) los reviews respecto al trato que el staff del hotel les dio a los visitantes.

9. Para este topic, las palabras más relevantes son: `open`, `art`, `history`, `roof`, `window`, `style`, `ancient`, `hallway`, `store` y `corridor`. La interpretación que le doy a este topic es que relaciona (principalmente) los reviews respecto a la arquitectura del hotel y/o lugares que visitaron durante su estadia.
