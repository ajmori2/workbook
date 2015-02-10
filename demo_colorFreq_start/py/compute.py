# imports/modules
import os
import random
import json
import collections
from PIL import Image

# Convert (r, g, b) into #rrggbb color
def getRGBstring( (r, g, b) ):
	s = "#"
	s = s + format(r, '02x')
	s = s + format(g, '02x')
	s = s + format(b, '02x')
	return s
	

def do_compute():
	# Open the image
    origImgFile = 'res/bryce.jpg'
    origImg = Image.open(origImgFile)


	# Process the image
	



	# Save the processed information
    output = { 'file': origImgFile,
	           'freq': freq }
	
    f = open("res/freq.json",'w')
    s = json.dumps(output, indent = 4)
    f.write(s)
	
	

