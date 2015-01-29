
from PIL import Image, ImageFilter
import json

def pixelDist((r1,g1,b1), (r2,g2,b2)):
    return ((r1-r2)*(r1-r2) + (g1-g2)*(g1-g2) + (b1-b2)*(b1-b2))

def isNavy(p):
    return (pixelDist(p,(0,0,130)) < 10000)

def isBrightGreen(p):
    return (pixelDist(p,(50,200,50)) < 12000)

def makeGold((r,g,b)):
    return (255,255,100)

def makeGreen((r,g,b)):
    return (0,120,0)

def packerfy(im):
    pack = im.copy()
    w,h = pack.size
    pixels = pack.load()

    for x in range(w):
        for y in range(h):
            if isNavy(pixels[x,y]):
                pixels[x,y] = makeGreen(pixels[x,y])
            elif isBrightGreen(pixels[x,y]):
                pixels[x,y] = makeGold(pixels[x,y])

    return pack

def do_compute():  #required for web app

    #set up file names to use for I/O
    orig_name = "res/ssfans.jpg"
    new_name = "res/packerfy2.jpg"

    # bring data into memory
    orig = Image.open(orig_name)

    justice = packerfy(orig)
    justice.save(new_name)

    # build list of dictionary(s) containing orig and new
    outData = [{'orig': orig_name, 'new': new_name }]

    with open('res/data.json','w') as outfile:
        json.dump(outData, outfile, indent=4, ensure_ascii=False)


