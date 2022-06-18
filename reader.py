import os

from collections import Counter
from os import walk
from os.path import splitext
from os.path import join

foodir = "./python-3.10.5-docs-text"
barlist = list()

for root, dirs, files in walk(foodir):
  for f in files:
    if splitext(f)[1].lower() == ".txt":
      barlist.append(join(root, f))

directory = './python-3.10.5-docs-text'

parsed = open('parsed.txt', 'w')
for i in barlist:
    file = open(i, 'r')
    
    for i in file.readlines():
        parsed.write(i)
    file.close()

parsed.close()