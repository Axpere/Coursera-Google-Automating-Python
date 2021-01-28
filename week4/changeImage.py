#!/usr/bin/env python3
import os, sys
from PIL import Image

path = "supplier-data/images/"
size = (600,400)

for pic in os.listdir(path):
  if 'tiff' in pic:
    #grab the picture name without the .tiff extension
    file, ext = os.path.splitext(pic)
    end_file = path + file + ".jpeg"
    try:
      Image.open(path + pic).convert("RGB").resize(size).save(end_file,"JPEG")
    except IOError:
      print("cannot convert: ", pic)

#This works
