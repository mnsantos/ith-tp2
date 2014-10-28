#!/usr/bin/python
import sys
import os
from glob import glob

DIR_OS = ""
DIR_WEKA = ""

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

def extract_attributes_for_wavs_in_path(path):
  for filename in glob(os.path.join(path, '*.wav')):
    name = filename[11:len(filename)-4]
    
    os.system(DIR_OS + "SMILExtract -C " + DIR_OS +  "config/IS10_paraling.conf -I " + filename + \
    " -O output.arff -instname " + name)
    os.system("rm smile.log")

  f = open("output.arff", "r")
  lines = f.readlines()
  for i in range(0,len(lines)):
    line = lines[i]
    if "@attribute numeric_class numeric" in line:
      line = "@attribute gender {m,f}\n"
    if line[0]=="'":
      line = line.split(",")
      genero = line[0][len(line[0])-2]
      line[-1] = genero
      line = ",".join(line)
      line = line + "\n"
    lines[i] = line 
  lines = "".join(lines)
  f = open("output.arff", "w")
  f.write(lines)

def extract_attributes_for_wav(filename):
  name = filename[:len(filename)-4]
  os.system(DIR_OS + "SMILExtract -C " + DIR_OS +  "config/IS10_paraling.conf -I " + filename + \
  " -O output-wav.arff -instname " + name)
  os.system("rm smile.log")

  f = open("output-wav.arff", "r")
  lines = f.readlines()
  for i in range(0,len(lines)):
    line = lines[i]
    if "@attribute numeric_class numeric" in line:
      line = "@attribute gender {m,f}\n"
    if line[0]=="'":
      line = line.split(",")
      genero = line[0][len(line[0])-2]
      line[-1] = genero
      line = ",".join(line)
      line = line + "\n"
    lines[i] = line 
  lines = "".join(lines)
  f = open("output.arff", "w")
  f.write(lines)

def filter_attributes(attr,inp,output):
  command = 'java -cp ' + DIR_WEKA + 'weka.jar weka.filters.unsupervised.attribute.Remove ' + \
            '-V -R ' + attr + ' -i ' + inp + ' -o ' + output
  print command
  os.system(command)

if __name__ == '__main__':
  filename = sys.argv[1]
  dirs = set_dirs()
  DIR_OS = dirs[0]
  DIR_WEKA = dirs[1]

  #path = "../tp2-dev/"
  #extract_attributes_for_wavs_in_path(path)

  extract_attributes_for_wav(filename)
  filter_attributes("685,1441,1432,1442,676,686,684,1440,712,713,671,1446,1584","output.arff", "output-filter.arff")