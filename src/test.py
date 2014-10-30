#!/usr/bin/python
import sys
import os
from glob import glob

def test(path):
  n = 0
  aciertos = 0
  errores = 0
  for filename in glob(os.path.join(path, '*.wav')):
    n = n + 1
    os.system('./genero.py ' + filename + " > result.txt")
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
  print "Aciertos: " + str(aciertos)
  print "Errores: " + str(errores)
  print "Porcentaje de efectividad: " + str((float(aciertos)/n)*100) + "%"


if __name__ == '__main__':
  path = sys.argv[1]
  test(path)