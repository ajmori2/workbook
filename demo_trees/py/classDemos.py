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
    
    textFile = '../res/ofk_ch1Short.txt'
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
        
    f = open("../res/trees.json",'w')
    s = json.dumps(nerTrees, indent = 4)
    f.write(s)

    return nerTrees    