# imports/modules
import os
import random
import json
from PIL import Image

def trunc(c,k): #truncates c to nearest multiple of k <= c
    return (k * (c/k))

def truncColor((r,g,b)): #truncates color components to mult of 8
    return (trunc(r,64),trunc(g,64),trunc(b,64))

def truncImage(origImg): #returns new truncated image
    w,h = origImg.size
    pixels = origImg.load()
    truncImg = Image.new("RGB", (w, h), "white")
    newPix = truncImg.load()
    for x in range(w):
        for y in range(h):
            newPix[x,y] = truncColor(pixels[x,y])
    return truncImg

def do_compute():
    # create a list of img file names
    imgs = os.listdir('res')

    # prepend "res/" to the file names
    imgs = ['res/' + f for f in imgs if ( f[-4:]=='.jpg' and not ('trunc.jpg' in f))]

    #choose a random image file to color truncate
    origImgFile = random.choice(imgs)
    
    #open and load that image
    origImg = Image.open(origImgFile)

    #truncate its color
    truncImg = truncImage(origImg)

    #write truncated image to a file for the web
    truncImgFile = origImgFile[:-4]+'_trunc.jpg'
    truncImg.save(truncImgFile,"JPEG")

    #throw the pair of file names into a list for the json
    outData = [ { 'orig': origImgFile, 'trunc': truncImgFile}]
        
    #create the json
    f = open("res/data.json",'w')
    f.write(json.dumps(outData,indent=4))

