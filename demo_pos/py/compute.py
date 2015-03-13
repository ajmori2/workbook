import json
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import TextTilingTokenizer
from nltk import pos_tag
from nltk import ne_chunk
from collections import defaultdict        
    
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
    #then we record their association.
    
    edgeParagraphs = defaultdict(list)
    for i,p in enumerate(paraPeople):
        uniqueNamesPara = set(p)
        for s in sorted(uniqueNamesPara):
            for t in sorted(uniqueNamesPara):
                if s<t:
                    edgeParagraphs[(s,t)].append(i)   
    
    #assemble list of edges and vertices
    #this is ugly because the d3 demands that we refer to 
    #endpoints by their location in the vertex list
    edges = []
    vertices = []
    for (s,t) in edgeParagraphs:
        wt = len(edgeParagraphs[(s,t)])
        if wt > 5: # demand frequent interaction
            if {'text':s} not in vertices:
                vertices.append({'text':s})
            if {'text':t} not in vertices:
                vertices.append({'text':t})      
            edges.append({'source': vertices.index({'text':s}), 
                          'target': vertices.index({'text':t}),
                          'wt': wt})

    outData = {'vertices': vertices,'edges': edges}
        
    f = open("res/graph.json",'w')
    s = json.dumps(outData, indent = 4)
    f.write(s)    