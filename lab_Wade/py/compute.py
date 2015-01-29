
#grab the python imaging library
from PIL import Image, ImageFilter
import json

#http://stackoverflow.com/questions/24152553/hsv-to-rgb-and-back-without-floating-point-math-in-python
def RGB_2_HSV(RGB):
    ''' Converts an integer RGB tuple (value range from 0 to 255) to an HSV tuple '''

    # Unpack the tuple for readability
    R, G, B = RGB

    # Compute the H value by finding the maximum of the RGB values
    RGB_Max = max(RGB)
    RGB_Min = min(RGB)

    # Compute the value
    V = RGB_Max;
    if V == 0:
        H = S = 0
        return (H,S,V)


    # Compute the saturation value
    S = 255 * (RGB_Max - RGB_Min) // V

    if S == 0:
        H = 0
        return (H, S, V)

    # Compute the Hue
    if RGB_Max == R:
        H = 0 + 43*(G - B)//(RGB_Max - RGB_Min)
    elif RGB_Max == G:
        H = 85 + 43*(B - R)//(RGB_Max - RGB_Min)
    else: # RGB_MAX == B
        H = 171 + 43*(R - G)//(RGB_Max - RGB_Min)

    return (H, S, V)

#http://stackoverflow.com/questions/24152553/hsv-to-rgb-and-back-without-floating-point-math-in-python
def HSV_2_RGB(HSV):
    ''' Converts an integer HSV tuple (value range from 0 to 255) to an RGB tuple '''

    # Unpack the HSV tuple for readability
    H, S, V = HSV

    # Check if the color is Grayscale
    if S == 0:
        R = V
        G = V
        B = V
        return (R, G, B)

    # Make hue 0-5
    region = H // 43;

    # Find remainder part, make it from 0-255
    remainder = (H - (region * 43)) * 6; 

    # Calculate temp vars, doing integer multiplication
    P = (V * (255 - S)) >> 8;
    Q = (V * (255 - ((S * remainder) >> 8))) >> 8;
    T = (V * (255 - ((S * (255 - remainder)) >> 8))) >> 8;


    # Assign temp vars based on color cone region
    if region == 0:
        R = V
        G = T
        B = P

    elif region == 1:
        R = Q; 
        G = V; 
        B = P;

    elif region == 2:
        R = P; 
        G = V; 
        B = T;

    elif region == 3:
        R = P; 
        G = Q; 
        B = V;

    elif region == 4:
        R = T; 
        G = P; 
        B = V;

    else: 
        R = V; 
        G = P; 
        B = Q;


    return (R, G, B)


def do_compute():  #required for web app

    #import os
    #set up file names to use for I/O

    orig_name = "res/packers.jpg"
    new_name = "res/packersNEW.jpg"

    # bring data into memory
    orig = Image.open(orig_name)
    pixels = orig.load()
    width,height = orig.size

    # make changes to data, creating new image
    for i in range(200):
        pixels[i, i] = (255,0,0)

    for x in range(width):
        for y in range(height):
        	r, g, b = pixels[x, y]
        	
        	h, s, v = RGB_2_HSV(pixels[x, y])
        	

        	# Orange: h = 26  / 360   ==>  18 / 255
        	# Blue:   h = 211 / 360   ==> 150 / 255
        	
        	#  <---- 18 ----- 84 ----- 150 ----- 212 ----->
        	#      orange     |        blue       |     orange
        	        	
        	if h >= 84 and h <= 212:
        		h = 150
        	else:
        		h = 18
        	
        	# Result 2:
        	# - Change sat. values for more color
        	#if s < 128:
        	#	s = s + 128
        	#else:
        	#	s = 255
        	
        	# Result 3:
        	# - Change value for HDR-like rendeirng:
        	#if v < 128:
        	#	#v = (v / 128) * 100
        	#	v = 0
        	#else:
        	#	v = int(((v - 128) / float(128)) * 200) + 55
        	       		
        	r, g, b = HSV_2_RGB( (h, s, v) )
        	
        	        		
        	pixels[x, y] = (r,g,b)
            
            
    # write data to file
    orig.save(new_name)

    # build list of dictionary(s) containing orig and new
    outData = [{'orig': orig_name, 'new': new_name }]

    with open('res/data.json','w') as outfile:
        json.dump(outData, outfile, indent=4, ensure_ascii=False)

