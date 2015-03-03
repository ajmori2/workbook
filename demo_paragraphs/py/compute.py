import json
import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import TextTilingTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from collections import Counter
from collections import defaultdict
from math import log, sqrt

def cosSim(a, b): 
    #parameters are dictionaries of tfidf measures for words
    #for this function we need the inner product of a and b, and the
    #lengths of each vector
    
    inner = 0
    sumsqA = 0
    sumsqB = 0
    for w in a:
        sumsqA += a[w] * a[w]
        if w in b:
            inner += a[w] * b[w]
    for w in b:
        sumsqB += b[w] * b[w]
    sim = float(inner)/(sqrt(sumsqA)*sqrt(sumsqB))
    return sim
 
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
    match = r'\n\n\n\n'
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

    #set up initial word tokens for each paragraph
    paraWords = [word_tokenize(p.decode('utf8')) for p in paragraphs]
    #clean each paragraph    
    paraWords = [clean(p) for p in paraWords]    

    #compute document frequency (df) for each word
    df = Counter()
    D = len(paraWords)
    for w in uniqueWords:
        for p in paraWords:
            if w in p:
                df[w] += 1
    
    #compute tfidf for each paragraph - uses df
    tfidf = []
    for p in paraWords:
        freq = makeFreq(p)
        tfidfPara = defaultdict()
        for w in freq:
            tfidfPara[w] = freq[w] * (log(D) - log(df[w]))
        tfidf.append(tfidfPara)
    
    #assemble list of vertices
    vertices = []
    for k in range(len(paragraphs)):
        vertices.append({'id':k,
                         'text':paragraphs[k]})
    
    numVert = len(vertices) 
    #assemble list of edges
    edges = []
    for source in range(numVert):
        for destination in range(source+1,numVert):
            cosSimilarity = cosSim(tfidf[source],tfidf[destination])                
            edges.append({'source': source, 
                          'target': destination,
                          'wt': cosSimilarity})

    outData = {'vertices': vertices,'edges': edges}
    #i = 0
    #for p in tfidf:
    #    textTfidf = {'desc': 'para'+str(i),
    #            'freq': p}
    #    outData.append(textTfidf)
    #    i += 1
        
    f = open("res/graph.json",'w')
    s = json.dumps(outData, indent = 4)
    f.write(s)

