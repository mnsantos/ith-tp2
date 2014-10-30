#!/usr/bin/python
import sys
import os
from glob import glob

def test(path):
  for filename in glob(os.path.join(path, '*.wav')):
    os.system('./genero.py ' + filename + " > result.txt")
    f = open("result.txt", "r")
    line = f.readlines()
    if "-m" in filename:
      if "m" in line[0]:
        print filename + " ...ok"
      elif "f" in line[0]:
        print filename + " ...error" + " resultado: f" 
      else:
        print "Algo raro paso"
    elif "-f" in filename:
      if "f" in line[0]:
        print filename + " ...ok"
      elif "m" in line[0]:
        print filename + " ...error" + " resultado: m"
      else:
        print "Algo raro paso"
    os.system("rm result.txt")


if __name__ == '__main__':
  path = sys.argv[1]
  test(path)