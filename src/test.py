#!/usr/bin/python
import sys
import os
from glob import glob

# NAME: test
# IN: pathFiles: path donde se encuentran los tests. 
#     pathModels: path donde se encuentran los modelos a testear.
# OUT: "result_models.txt" en donde se encuentran los resultados de los tests para cada modelo.
# La funcion toma los dos paths pasados como parametros y evalua cada modelo de pathModelos con
# el conjunto de tests en pathFiles. Para ello tiene en cuenta la cantidad de aciertos y de errores
# y nos da un porcentaje de efectividad.

def test(pathFiles, pathModels):
  for model in glob(os.path.join(pathModels, '*.model')):
    aciertos = 0
    errores = 0
    n = 0
    for filename in glob(os.path.join(pathFiles, '*.wav')):
      n = n + 1
      os.system('./genero.py ' + filename + " " + model + " > result.txt")
      f = open("result.txt", "r")
      line = f.readlines()
      if "-m" in filename:
        if "m" in line[0]:
          print filename + " ...ok"
          aciertos = aciertos + 1
        elif "f" in line[0]:
          print filename + " ...error" + " resultado: f"
          errores = errores + 1 
        else:
          print "Algo raro paso"
      elif "-f" in filename:
        if "f" in line[0]:
          print filename + " ...ok"
          aciertos = aciertos + 1
        elif "m" in line[0]:
          print filename + " ...error" + " resultado: m"
          errores = errores + 1
        else:
          print "Algo raro paso"
      os.system("rm result.txt")

    print "--------------------------------------"

    results = open("results_models.txt", "a")
    results.write("Resultados para modelo " + model + ":\n")  
    results.write("Aciertos: " + str(aciertos) + "\n")
    results.write("Errores: " + str(errores) + "\n")
    results.write("Porcentaje de efectividad: " + str((float(aciertos)/n)*100) + "%\n")

if __name__ == '__main__':

  pathFiles = sys.argv[1]
  pathModels = sys.argv[2]
  test(pathFiles, pathModels)