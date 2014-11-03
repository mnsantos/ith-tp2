#!/usr/bin/python
import sys
import os
from glob import glob

DIR_OS = ""
DIR_WEKA = ""

# NAME: set_dirs()
# La funcion setea los paths de open-smile y weka.

def set_dirs():
  f = open("config.cfg", "r")
  lines = f.readlines()
  for line in lines:
    if "DIR_WEKA" in line:
      line = line.split()
      DIR_WEKA = line[1]
    if "DIR_OPEN-SMILE" in line:
      line = line.split()
      DIR_OS = line[1]
  return [DIR_OS,DIR_WEKA]

# NAME: extract_attributes_for_wav
# IN: filename
# La funcion extrae los atributos del .wav haciendo uso de la herramienta open-smile. Luego filtra el atributo
# "name" y guarda un .arff llamado "output-wav.arff" con los valores de cada atirubto.

def extract_attributes_for_wav(filename):
  os.system(DIR_OS + "SMILExtract -C " + DIR_OS +  "config/IS10_paraling.conf -I " + filename + \
  " -O output-wav.arff > /dev/null 2>&1")
  os.system("rm smile.log")

  f = open("output-wav.arff", "r")
  lines = f.readlines()
  for i in range(0,len(lines)):
    line = lines[i]
    if "@attribute numeric_class numeric" in line:
      line = "@attribute gender {m,f}\n"
    if line[0]=="'":
      line = line.split(",")
      line[-1] = "?"
      line = ",".join(line)
      line = line + "\n"
    lines[i] = line 
  lines = "".join(lines)
  f = open("output-wav.arff", "w")
  f.write(lines)

# NAME: filter_attributes
# IN: array de atributos, input, output
# La funcion toma el input pasado como parametro y remueve todos los atributos que no se encuentran en el array
# de atributos. Guarda los resultados en output.

def filter_attributes(attr, inp, output):
  command = 'java -cp ' + DIR_WEKA + 'weka.jar weka.filters.unsupervised.attribute.Remove ' + \
            '-V -R ' + attr + ' -i ' + inp + ' -o ' + output
  os.system(command)

# NAME: classify
# IN: model
# OUT: "m" o "f"
# La funcion utiliza el modelo pasado como parametro para clasificar el .wav como "m" o "f" y retorna el resultado.

def classify(model):
  weka = "weka.classifiers."
  if "forest" in model:
    weka = weka + "trees.RandomForest"
  elif "jrip" in model:
    weka = weka + "rules.JRip"
  elif "j48graft" in model:
    weka = weka + "trees.J48graft"
  elif "j48" in model:
    weka = weka + "trees.J48"
  elif "tree" in model:
    weka = weka + "trees.RandomTree"
  elif "smo" in model:
    weka = weka + "functions.SMO" 
  elif "bayes" in model:
    weka = weka + "bayes.NaiveBayes"

  os.system("java -cp " + DIR_WEKA + "weka.jar " + weka + " -l " + model + " -T output-wav.arff -p 0 > result 2>&1")
  f = open("result", "r")
  lines = f.readlines()
  for line in lines:
    if ":m" in line:
      return "m"
    elif ":f" in line:
      return "f"

if __name__ == '__main__':
  filename = sys.argv[1]
  model = sys.argv[2]

# Seteamos los paths de Opensmile y Weka con los parametros establecidos en config.cfg.

  dirs = set_dirs()
  DIR_OS = dirs[0]
  DIR_WEKA = dirs[1]

# Extraemos los 1500 atributos del .wav pasado como parametro con la herramienta open-smile.

  extract_attributes_for_wav(filename)

# Filtramos el atributo "name" 

  os.system('java -cp ' + DIR_WEKA + 'weka.jar weka.filters.unsupervised.attribute.Remove ' + \
            '-R 1 -i output-wav.arff -o output1.arff')
  os.system("mv output1.arff output-wav.arff")

# Filtramos nuevamente los atributos quedandonos con un conjunto reducido cuyo tamaño maximo es 40.

  filter_attributes("255,278,675,683,685,711,1439,1440,1583","output-wav.arff", "output-wav1.arff")
  os.system("mv output-wav1.arff output-wav.arff")

# Clasificamos el .wav pasado como parametro y mostramos el resultado por pantalla.

# model = 
  print classify(model)
  os.system("rm output-wav.arff")
  os.system("rm result")
