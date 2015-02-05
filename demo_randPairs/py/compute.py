# imports/modules
import os
import random
import json

def pairsList(imgList,k):
    retImgs = []
    for i in range(k):
        onePair = {"left": random.choice(imgList),
                   "right": random.choice(imgList)}
        retImgs.append(onePair)
        
    return retImgs
        

def do_compute():
    # create a list of img file names
    #s = os.path.join(os.getcwd(), "py/../../res")
    s = 'res'
    imgs = os.listdir(s)

    # prepend "res/" to the file names
    imgs = ['res/' + f for f in imgs if f[-4:]=='.jpg']

    # create a list of random pairs of imgs
    
    randImgs=pairsList(imgs,12)
        
    #print(randImgs)
        
    f = open("res/data.json",'w')
    f.write(json.dumps(randImgs,indent=4))
    #print(json.dumps(randImgs,indent=4))#print data to json file

