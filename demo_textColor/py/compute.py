import json
from nltk.tokenize import word_tokenize
from collections import Counter

def makeFreq(textFile,colorNames):
    textRaw = open(textFile).read()
    words = word_tokenize(textRaw.decode('utf8'))
    words = [w.lower() for w in words]

    #tally color words from the text
    freq = Counter()
    for w in words:
        if w in colorNames:
            freq[w] += 1
           
    textFreq = { 'file': textFile,
	           'freq': freq }
    return textFreq
    
def do_compute():

    #load the color name files
    colorNamesFile = 'res/colorNames.txt'
    colorRaw = open(colorNamesFile).read()
    colorNames = word_tokenize(colorRaw)
    
    outData = []
    #build the freq table
    textDict = makeFreq('res/hg.txt',colorNames)
	 #Save the processed information
    outData.append(textDict)  
    
    textDict = makeFreq('res/cf.txt',colorNames)
	 #Save the processed information
    outData.append(textDict)
    
    textDict = makeFreq('res/mj.txt',colorNames)
	 #Save the processed information
    outData.append(textDict)
    
    f = open("res/freq.json",'w')
    s = json.dumps(outData, indent = 4)
    f.write(s)

