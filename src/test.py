#!/usr/bin/python
import sys
import os
from glob import glob

def test(path):
  for filename in glob(os.path.join(path, '*.wav')):
    print './genero.py ' + filename + " > result.txt"
    os.system('./genero.py ' + filename + " > result.txt")
    f = open("result.txt", "r")
    line = f.readlines()
    print line
    if "-m" in filename:
      if "m" in line[0]:
        print filename + " ...ok"
      else:
        print filename + " ...error"
    elif "-f" in filename:
      if "f" in line[0]:
        print filename + " ...ok"
      else:
        print filename + " ...error"
    os.system("rm result.txt")


if __name__ == '__main__':
  path = sys.argv[1]
  test(path)