import json
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from collections import Counter
    
def makeFreq(title,words):
    freq = Counter()
    for w in words:
        freq[w] += 1
    freq_table = dict(freq.most_common(30))
    
    textFreq = {'desc': title,
                'freq': freq_table}
    return textFreq    
    
def do_compute():
    ''' output:  json file containing a sequence of 
                frequency tables illustrating the steps
                required for general text cleaning.'''
                
    
    textFile = 'res/hg.txt'
    textRaw = open(textFile).read() #textRaw is now a string
    
    #custom preprocessing on raw string.
    match = r'\d+ \| P a g e'
    textRaw = re.sub(match,'',textRaw)
    match = r'The Hunger Games - Suzanne Collins'
    textRaw = re.sub(match,'',textRaw)    
 
    outData = [] # container in which we'll put freq tables

    #set up initial tokens
    words = word_tokenize(textRaw.decode('utf8'))
    textFreq = makeFreq('tokens',words)               
    outData.append(textFreq)
    
    #make words lower case
    words = [w.lower() for w in words]
    textFreq = makeFreq('lower case',words)
    outData.append(textFreq)

    #remove period from end of sentences
    #get rid of punctuation and other non-alpha
    words = [re.sub('\.$', '',w) for w in words]
    words = [w for w in words if w.isalpha()]    
    textFreq = makeFreq('remove punctuation etc',words)
    outData.append(textFreq)
    
    #remove stop words
    words = [w for w in words if not w in stopwords.words('english')]
    textFreq = makeFreq('remove stop words',words)
    outData.append(textFreq)
    
    #do stemming "goes" => "go"
    words = [SnowballStemmer('english').stem(w) for w in words]
    textFreq = makeFreq('remove stop words',words)
    outData.append(textFreq)

    f = open("res/freq.json",'w')
    s = json.dumps(outData, indent = 4)
    f.write(s)

