# imports/modules
#import os
#import random
import json
import re
#import collections
#from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import word_tokenize
from collections import defaultdict
from csv import DictReader


# Convert (r, g, b) into #rrggbb color
def getRGBstring( (r, g, b) ):
    s = "#"
    s = s + format(int(r), '02x')
    s = s + format(int(g), '02x')
    s = s + format(int(b), '02x')
    return s


def do_compute():

    #load the color name files
    colorNamesFile = 'res/colorNames.csv'
    colorRaw = open(colorNamesFile)
    reader = DictReader(colorRaw,skipinitialspace=True)
    
    colorData = defaultdict(str)
    colorNames = []
    for row in reader:
        colorData[row['name']] = row['rgb']
        colorNames.append(row['name'])
 

	# Open the text
    textFile = 'res/hg.txt'
    textRaw = open(textFile).read()
    words = word_tokenize(textRaw)
    print words[:130]


    freq = defaultdict(int)
    for w in words:
        if w in colorNames:
            freq[w] += 1
                    

    colorHex = defaultdict(str)
    for color in colorData:
        c = re.split('\D',colorData[color])[1:4]
        colorHex[color] = getRGBstring(c)
        
        
    # freq:
    #   { "blue": 100,
    #     "gray": 200,
    #     "gold": 300,
    #     ...
    #    }
    
	# Save the processed information
    output = { 'file': textFile,
	           'freq': freq,
              'nameHex': colorHex }
	
    f = open("res/freq.json",'w')
    s = json.dumps(output, indent = 4)
    f.write(s)

	
 

