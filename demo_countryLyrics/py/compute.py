import json
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

def makeFreq(textFile,colorNames):
    with open (textFile) as data_file:
        jsondata = json.load(data_file)
        freq = Counter()
        
        # Look at the word diversity by author
        author_freq = {}
        for data in jsondata:
            
            # artist name
            artist = data['artist'][0]
            
            # Text processing chain
            textRaw = data['text']
            text = ' '.join(textRaw)
            text = ''.join([i if ord(i) < 128 else ' ' for i in text])
            words = word_tokenize(text.decode('ascii'))
            words = [w.lower() for w in words]
            words = [re.sub('\.$', '',w) for w in words]
            words = [w for w in words if w.isalpha()]
            words = [w for w in words if not w in stopwords.words('english')]
            
            # Create w word counter if it doesn't exist for that artist
            if artist not in author_freq:
                author_freq[artist] = Counter()
            
            # Count the occurences of each word for a given author
            for w in words:
                #if interested, tally color words from the text
                #if w in colorNames:
                #    freq[w] += 1
                author_freq[artist][w] += 1
        
        # We only use distinct counts for each artist -- but could also count total words
        # For better results (% novel words of total)
        onlydistinct = {}
        for author in author_freq:
            onlydistinct[author] = len(author_freq[author])
        
        #aFreq = { 'file': textFile,
        #            'freq': author_freq }
        #return author_freq

        return onlydistinct

def do_compute():

# Color processing if interested
#    load the color name files
#    colorNamesFile = 'res/colorNames.txt'
#    colorRaw = open(colorNamesFile).read()
#    colorNames = word_tokenize(colorRaw)

    outData = []
    
    #build the freq table
    textDict = makeFreq('res/lyrics.json',colorNames)
    
	 #Save the processed information
    outData.append(textDict)

    f = open("res/freq.json",'w')
    s = json.dumps(outData, indent = 4)
    f.write(s)

do_compute()
