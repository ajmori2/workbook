import json
from nltk.tokenize import word_tokenize
from collections import Counter

def do_compute():

    #load the color name files
    colorNamesFile = 'res/colorNames.txt'
    colorRaw = open(colorNamesFile).read()
    colorNames = word_tokenize(colorRaw)
    
	 #Open the text
    textFile = 'res/hg.txt'
    textRaw = open(textFile).read()
    words = word_tokenize(textRaw.decode('utf8'))
    words = [w.lower() for w in words]

    #tally color words from the text
    freq = Counter()
    for w in words:
        if w in colorNames:
            freq[w] += 1
        
    # freq:
    #   { "blue": 100,
    #     "gray": 200,
    #     "gold": 300,
    #     ...
    #    }
    
	# Save the processed information
    output = { 'file': textFile,
	           'freq': freq }
	
    f = open("res/freq.json",'w')
    s = json.dumps(output, indent = 4)
    f.write(s)

