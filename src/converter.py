#!/usr/bin/python
import sys
import os
from glob import glob

def convert_files(path):
  number = 1
  for root, dirs, files in os.walk(path):
    for f in files:
      if (f.endswith('.aac')):
        if not root.endswith('/'):
          root = root + '/'
        command = 'ffmpeg -i ' + root + f + " ../test/" + '%03d' % number + '.wav'
        os.system(command)
        number = number + 1 
  print number

if __name__ == '__main__':
  path = sys.argv[1]
  convert_files(path)
