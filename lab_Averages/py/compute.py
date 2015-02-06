
#grab the python imaging library
from PIL import Image, ImageFilter
import json
import os
import random

def average(num1,num2):
    # average of two numbers
    # note we truncate before adding, not after


    return avg

def take_Average(px1,px2,pixels,width,height):
    
    # For every pixel in the smaller dimensions

            
            # Get current RGB values


            # Average them
            r = average(r1,r2)
            g = average(g1,g2)
            b = average(b1,b2)
            
            # set current pixel value to the averages


    # return result
    return pixels


def process_ImgFiles(fn1,fn2):
    
    # load the two images
    # including current pixel values

    # get the size of each image

    # Note that a problem you need to address is what happens if your
    # two images are not the same size. Here we take the simple approach
    # that we only average in the smaller of each of the dimensions.
    # You can think about how else you might solve this problem and
    # implement your own approach if you like.
    # only operate on the smaller dimensions
    width = min(width1,width2)
    height = min(height1,height2)
    
    # Create a new Image with the minimum dimensions
    # This is what we will use to store the average
    im = Image.new('RGB', (width,height), "white")
    avgpixels = im.load()
    
    # Get the average from the two images you just loaded
    avgpixels = take_Average(pixels1,pixels2,avgpixels,width,height)
    
    # Return the average image up to do_compute
    return im

def do_compute():  #required for web app

    # Get a list of all the filenames in the resources (res) directory
    filenames =
    
    
    # Check that they are images
    # Check that they are not already averaged (note the naming convention for average images on line 83)
    # Prepend the directory (res) on to the front of the filename
    # Make sure the output here is also a list
    img_filenames =
    
    # Initialize a list of the output data you'll be creating
    outData =
    
    # Create five separate results, each of which should select a random pair of images and show those two images and the averaged result.
    # Loop through five times
    

        # Pick two files at random to average
        # Make sure that the second filename is not the same as the first
        fn1 =
        fn2 =
        
        # Create a new filename that you'll use to save the output
        # If the two files you chose were named "1.jpg" and "2.jpg"
        # Your resulting filename should follow the format:
        # "1_2avg.jpg"
        new_fn =
    
        # Process the two images associated with the random filenames chosen, including finding the average. Return an image with the average values.
        im = process_ImgFiles(fn1,fn2)
    
        # Save the image with the average values to the filename you just created
        
    
        # Build list of dictionary(s) containing origal images and new
        # Filename 1 should have key fn1
        # Filename 2 should have key fn2
        # The averaged image should have key avg
        outData.append()

    # output the data in a format readable by the workbook
    with open('res/data.json','w') as outfile:
        json.dump(outData, outfile, indent=4, ensure_ascii=False)

