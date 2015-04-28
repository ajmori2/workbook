import json
import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import TextTilingTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from collections import Counter
from collections import defaultdict
from math import log
    
def makeFreq(words):
    freq = Counter()
    for w in words:
        freq[w] += 1
    return freq
        
    
def clean(words):
    words = [w.lower() for w in words]
    words = [re.sub('\.$', '',w) for w in words]
    words = [w for w in words if w.isalpha()]
    words = [w for w in words if not w in stopwords.words('english')]
    words = [SnowballStemmer('english').stem(w) for w in words]
    return words
    
    
def do_compute():
    ''' output:  json file containing a sequence of 
                frequency tables illustrating the steps
                required for general text cleaning.'''
                
    textFile = 'res/hgShort.txt'
    textRaw = open(textFile).read() #textRaw is now a string

    #custom preprocessing on raw string.
    match = r'\d+ \| P a g e'
    textRaw = re.sub(match,'',textRaw)
    match = r'The Hunger Games - Suzanne Collins'
    textRaw = re.sub(match,'',textRaw)    
 
    #tokenize the text into paragraphs (takes a long time).
    ttt = TextTilingTokenizer()
    paragraphs = ttt.tokenize(textRaw)
    #write it out so we don't have to compute it again
    f = open("res/paragraphs.json",'w')
    s = json.dumps(paragraphs, indent = 4)
    f.write(s)
    
    #tokenize words for idf computation
    words = word_tokenize(textRaw.decode('utf8'))
    words = clean(words)
    uniqueWords = set(words)

    #set up initial tokens
    paraWords = [word_tokenize(p.decode('utf8')) for p in paragraphs]
    #clean each paragraph    
    paraWords = [clean(p) for p in paraWords]    

    #compute df
    df = Counter()
    D = len(paraWords)
    for w in uniqueWords:
        for p in paraWords:
            if w in p:
                df[w] += 1
    
    tfidf = []
    for p in paraWords:
        freq = makeFreq(p)
        tfidfPara = defaultdict()
        for w in freq:
            tfidfPara[w] = freq[w] * (log(D) - log(df[w]))
        tfidf.append(tfidfPara)
    
    outData = []   
    i = 0
    for p in tfidf:
        textTfidf = {'desc': 'para'+str(i),
                'freq': p}
        outData.append(textTfidf)
        i += 1
        
    f = open("res/para.json",'w')
    s = json.dumps(outData, indent = 4)
    f.write(s)

