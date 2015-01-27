
from PIL import Image, ImageFilter
import json

def pixelDist((r1,g1,b1), (r2,g2,b2)):
    return ((r1-r2)*(r1-r2) + (g1-g2)*(g1-g2) + (b1-b2)*(b1-b2))

def isNavy(p):
    return (pixelDist(p,(0,0,130)) < 10000)

def isBrightGreen(p):
    return (pixelDist(p,(50,200,50)) < 12000)

def packerfy(im):
    pack = im.copy()
    w,h = pack.size
    pixels = pack.load()

    for x in range(w):
        for y in range(h):
            if isNavy(pixels[x,y]):
                pixels[x,y] = (0,110,0) #green
            elif isBrightGreen(pixels[x,y]):
                pixels[x,y] = (255,255,100) #yellow

    return pack

def do_compute():  #required for web app

    #set up file names to use for I/O
    orig_name = "static/demo_NFL/ssfans.jpg"
    new_name = "static/demo_NFL/packerfy.jpg"

    # bring data into memory
    orig = Image.open(orig_name)

    justice = packerfy(orig)
    justice.save(new_name)

    # build list of dictionary(s) containing orig and new
    outData = [{'orig': '/'+ orig_name, 'new': '/'+ new_name }]

    with open('static/demo_Welcome/data.json','w') as outfile:
        json.dump(outData, outfile, indent=4, ensure_ascii=False)


