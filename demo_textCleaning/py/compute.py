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

    textFreq = { 'desc': title,
	           'freq': freq_table }
    return textFreq
    
def do_compute():
    
    outData = []
    textFile = 'res/hg.txt'
    textRaw = open(textFile).read() #textRaw is now a string
    
    #custom preprocessing
    textRaw = re.sub(r'\d+ \| P a g e',' ',textRaw)
    textRaw = re.sub(r'The Hunger Games - Suzanne Collins',' ', textRaw)
    
    #set up initial tokens
    words = word_tokenize(textRaw.decode('utf8'))
    wordsFreq = makeFreq('tokens',words)         
    outData.append(wordsFreq)
    
    #make words lower case
    words = [w.lower() for w in words]
    wordsFreq = makeFreq('lower case',words)         
    outData.append(wordsFreq)
    
    #get rid of punctuation
    #remove period from end of sentences
    words = [re.sub('\.$','', w) for w in words]
    words = [w for w in words if w.isalpha()]
    wordsFreq = makeFreq('remove punctuation',words)         
    outData.append(wordsFreq)
    
    #stop words
    words = [w for w in words if not w in stopwords.words('english')]
    wordsFreq = makeFreq('remove stop words',words)         
    outData.append(wordsFreq)
    
    #do stemming "goes" => "go"
    words = [SnowballStemmer("english").stem(w) for w in words]
    wordsFreq = makeFreq('Snowball stemmed',words)         
    outData.append(wordsFreq)
    
    f = open("res/freq.json",'w')
    s = json.dumps(outData, indent = 4)
    f.write(s)

