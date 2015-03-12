import json
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import TextTilingTokenizer
from nltk import pos_tag
from nltk import ne_chunk
from collections import Counter
        
    
def traverse(t):
    try:
        t.label()
    except AttributeError:
        return []
    else:
        # Now we know that t.label is defined
        if t.label()=='PERSON':
            return [t.leaves()]
        else:
            ret = [] 
            for child in t:
                x = traverse(child)
                ret += x
            return ret  
            
def nameString(name):
    retString = ''
    for n in name:
        retString += n[0]
    return retString
    
def flatNames(para):
    retList = []
    for sent in para:
        retList += sent
    return retList
    
def do_compute():
    ''' output:  json file containing a sequence of 
                frequency tables illustrating the steps
                required for general text cleaning.'''
    return
    
    textFile = 'res/hp.txt'
    textRaw = open(textFile).read() #textRaw is now a string
    
    #tokenize the text into paragraphs (takes a long time).
    ttt = TextTilingTokenizer()
    paragraphs = ttt.tokenize(textRaw) 
    
    #tokenize sentences for NER
    #paragraphs -> sentences
    paraSents = [sent_tokenize(p.decode('utf8')) for p in paragraphs if p]
    
    #paragraphs -> sentences -> words
    paraSentWords = [[word_tokenize(s) for s in p if s] for p in paraSents]
 
    #paragraphs -> sentences -> tagged words
    paraSentPOS = [[pos_tag(s) for s in p] for p in paraSentWords]
 
    #parse sentences and label people
    nerTrees = [[ne_chunk(s) for s in p] for p in paraSentPOS]
    
    #extract people in each paragraph
    paraPeople = [[traverse(s) for s in p] for p in nerTrees]
    paraPeople = [[persons for persons in p if persons] for p in paraPeople]
    paraPeople = [[[nameString(n) for n in s] for s in p] for p in paraPeople]    
    paraPeople = [flatNames(p) for p in paraPeople]
    
    #if two people appear in the same paragraph
    #then we increment the strength of their
    #association
    
    edgeWeight = Counter()
    vertexWeight = Counter()    
    uniqueNames = set()
    for p in paraPeople:
        uniqueNamesPara = set(p)
        uniqueNames = uniqueNames.union(uniqueNamesPara)
        for s in uniqueNamesPara:
            for t in uniqueNamesPara:
                if s<t:
                    edgeWeight[(s,t)] += 1
                    vertexWeight[s] += 1
                    vertexWeight[t] += 1
                
    vertices = []
    for name in uniqueNames:
        vertices.append({'text':name,
                         'weight':vertexWeight[name]})
    
    #assemble list of edges
    edges = []
    numVert = len(vertices)
    for s in range(numVert):
        for t in range(s+1,numVert):
            wt = max(edgeWeight[vertices[s]['text'],vertices[t]['text']],
                     edgeWeight[vertices[t]['text'],vertices[s]['text']])
            if wt > 0:
                edges.append({'source': s, 
                          'target': t,
                          'wt': wt})

    outData = {'vertices': vertices,'edges': edges}
        
    f = open("res/graph.json",'w')
    s = json.dumps(outData, indent = 4)
    f.write(s)    