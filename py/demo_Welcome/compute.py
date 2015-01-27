
#grab the python imaging library
from PIL import Image, ImageFilter
import json

def do_compute():  #required for web app

    #set up file names to use for I/O
    orig_name = "static/demo_Welcome/packers.jpg"
    new_name = "static/demo_Welcome/packersNEW.jpg"

    # bring data into memory
    orig = Image.open(orig_name)
    pixels = orig.load()
    width,height = orig.size

    # make changes to data, creating new image
    for i in range(200):
        pixels[i, i] = (255,0,0)

    for x in range(width):
        for y in range(height):
            pixels[x,y] = (255,255,255)
    # write data to file
    orig.save(new_name)

    # build list of dictionary(s) containing orig and new
    outData = [{'orig': '/'+ orig_name, 'new': '/'+ new_name }]

    with open('static/demo_Welcome/data.json','w') as outfile:
        json.dump(outData, outfile, indent=4, ensure_ascii=False)

do_compute()
