#!/usr/bin/python
import sys
import os
from glob import glob

def extract_attributes():
  path = "../tp2-dev/"
  for filename in glob(os.path.join(path, '*.wav')):
    clase = filename[len(filename)-5]
    name = filename[11:len(filename)-4]
    
    os.system("SMILExtract -C ../opensmile-1.0.1-sourceonly/config/paraling_IS10.conf -I " + filename + \
    " -O output.arff -instname " + name + " -classes {m,f} -classlabel " + clase)

    os.system("rm smile.log")

if __name__ == '__main__':
  extract_attributes()

