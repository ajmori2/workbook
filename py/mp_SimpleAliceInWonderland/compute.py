from nltk.probability import FreqDist                                       
from nltk.corpus import PlaintextCorpusReader, stopwords
from nltk.stem import PorterStemmer
from operator import itemgetter
import json

def do_compute():

    # read text file into memory
    raw_text = PlaintextCorpusReader('static/mp_SimpleAliceInWonderland', 'AliceInWonderland.txt')

    #get the important words (data cleaning)
    words = raw_text.words()
    words = [w.lower() for w in words]
    words = [w for w in words if w.isalpha()]
    words = [w for w in words if not w in stopwords.words('english')]
    words = [PorterStemmer().stem(w) for w in words]

    #compute frequencies
    freq = FreqDist(words)

    #now that we've counted, remove duplicates from word list
    words = set(words)

    #build dictionary for json
    outData = []
    for w in words:
        outData.append({'word':str(w), 'freq':freq[w]})

    outDataSorted = sorted(outData, key=itemgetter('freq'), reverse=True)

    #dump dict to json file
    with open('static/mp_SimpleAliceInWonderland/data.json','w') as outfile:
        json.dump(outDataSorted[:20], outfile, sort_keys=True, indent=4, ensure_ascii=False)
    

do_compute()
