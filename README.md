
IMPORTANTE: ANTES DE UTILIZAR LOS SCRIPTS QUE SE ENCUENTRAN EN src/ SETEAR LOS PATHS DE WEKA y OPEN-SMILE EN config.cfg

Aclaraciones sobre los archivos en src:

extraer-atributos.py: 

Script utilizado para extraer los atributos de los wavs en /tp2-dev. Con estos atributos entrenamos un modelo de aprendizaje haciendo uso de WEKA. Forma de uso:
./extraer_atributos

genero.py: 

Script que determina el genero de la persona hablante del wav pasado como parametro. Para ello, extrae los atributos necesarios e invoca al modelo aprendido. Forma de uso:
./genero.py [archivo .wav]

test.py:

IMPORTANTE: para utilizar el script comentar la linea 118 de 'genero.py'. Tener en cuenta que los modelos a testear deben usar los mismos atributos. Estos se encuentran determinados en 'genero.py'.
Script que evalua el porcentaje de efectividad de los modelos en src/models. Forma de uso:

./test [path de los test] [path de los modelos]


