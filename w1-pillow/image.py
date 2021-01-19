#!/usr/bin/env python3

import os, sys #imports os and sys for directory operations
from PIL import Image #imports Image function from PIL or pillow library for image edition

#Defining output options
size = (128, 128) #pixel width and heigth
rotation = 270 #90 deg clockwise
end_dirc = "/opt/icons/" #destination

#obtain file names in the origin directory
for root, dirs, files in os.walk("/home/student-02-fd4579322602/images/"):
  for file in files: #iterate for each file (name)
   final_dirc = "/opt/icons/" + file #create final destination with directory + name
   try:
      with Image.open(file) as pic: #opens file as object
        #edits the image object, the RGB conversion is a necesary step in this case
        pic.rotate(rotation).resize(size).convert("RGB").save(final_dirc, "JPEG")
   except OSError:
      print("Cannot convert", file)
