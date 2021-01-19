#!/usr/bin/env python3

import os, sys
from PIL import Image

#Defining output options
size = (128, 128)
rotation = 270
end_dirc = "/opt/icons/"

for root, dirs, files in os.walk("/home/student-02-fd4579322602/images/"):
  for file in files:
   final_dirc = "/opt/icons/" + file
   try:
      with Image.open(file) as pic:
        pic.rotate(rotation).resize(size).convert("RGB").save(final_dirc, "JPEG")
   except OSError:
      print("Cannot convert", file)
