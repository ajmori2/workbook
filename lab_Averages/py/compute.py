
#grab the python imaging library
from PIL import Image, ImageFilter
import json
import os
import random

def average(num1,num2):
    # average of two numbers
    # note we truncate before adding, not after
    avg = num1/2 + num2/2
    return avg

def take_Average(px1,px2,pixels,width,height):
    
    # For every pixel in the smaller dimensions
    for x in range(width):
        for y in range(height):
            
            # Get current RGB values
            r1,g1,b1 = px1[x,y]
            r2,g2,b2 = px2[x,y]

            # Average them
            r = average(r1,r2)
            g = average(g1,g2)
            b = average(b1,b2)
            
            # set pixels to the averages
            #print r2,g2,b2
            pixels[x,y]= (r,g,b)

    # return result
    return pixels


def process_ImgFiles(fn1,fn2):
    
    # load the two images
    img1 = Image.open(fn1)
    pixels1 = img1.load()

    img2 = Image.open(fn2)
    pixels2 = img2.load()

    # get the size of each image
    width1,height1 = img1.size
    width2,height2 = img2.size

    # only operate on the smaller dimensions
    width = min(width1,width2)
    height = min(height1,height2)
    
    # new Image with min dimensions
    im = Image.new('RGB', (width,height), "white")
    avgpixels = im.load()
    
    avgpixels = take_Average(pixels1,pixels2,avgpixels,width,height)
    return im, avgpixels

def do_compute():  #required for web app

    # get filenames in res directory
    filenames = os.listdir('./res')
    #print filenames
    
    # check that they are images and not averages
    img_filenames = ["res/" + fn for fn in filenames if fn[-4:]==".jpg" and fn[-7:-4] != "avg"]
    
    outData = []
    
    # pick two at random to average
    num_results = 5
    for n in range(num_results):

        # pick two files at random to average
        fn1 = random.choice(img_filenames)
        fn2 = random.choice([x for x in img_filenames if x not in [fn1]])
        
        # new filename for saving
        new_fn = fn1[:-4] + "_" + fn2[4:-4] + "avg.jpg"
    
        # take the average of the two images
        im, pixels = process_ImgFiles(fn1,fn2)
    
        # Save file
        im.save(new_fn)
    
        # build list of dictionary(s) containing origal images and new
        outData.append({'fn1': fn1, 'fn2': fn2, 'avg' : new_fn})

    # output the data in a format readable by the workbook
    with open('res/data.json','w') as outfile:
        json.dump(outData, outfile, indent=4, ensure_ascii=False)

