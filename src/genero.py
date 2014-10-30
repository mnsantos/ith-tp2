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


def filter_attributes(attr,inp,output):
  command = 'java -cp ' + DIR_WEKA + 'weka.jar weka.filters.unsupervised.attribute.Remove ' + \
            '-V -R ' + attr + ' -i ' + inp + ' -o ' + output
  os.system(command)

def classify():
  os.system("java -cp " + DIR_WEKA + "weka.jar weka.classifiers.trees.RandomForest -l seingrandomforest3.model -T output-wav.arff -p 0 > result 2>&1")
  f = open("result", "r")
  lines = f.readlines()
  for line in lines:
    if ":m" in line:
      return "m"
    elif ":f" in line:
      return "f"

if __name__ == '__main__':
  filename = sys.argv[1]
  dirs = set_dirs()
  DIR_OS = dirs[0]
  DIR_WEKA = dirs[1]


  extract_attributes_for_wav(filename)

  os.system('java -cp ' + DIR_WEKA + 'weka.jar weka.filters.unsupervised.attribute.Remove ' + \
            '-R 1 -i output-wav.arff -o output1.arff')
  os.system("mv output1.arff output-wav.arff")

  filter_attributes("255,278,675,683,685,711,1439,1440,1583","output-wav.arff", "output-wav1.arff")
  os.system("mv output-wav1.arff output-wav.arff")
  print classify()
  os.system("rm output-wav.arff")
  os.system("rm result")
