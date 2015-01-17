import string
import collections

def do_compute():
    # Create a dictionary that will init missing values as ints (as 0)    
    wordList = collections.defaultdict(int)
    
    # Count the times each word appears in Alice in Wonderland
    f = open('static/mp_SimpleAliceInWonderland/AliceInWonderland.txt', 'r');

    for line in f:
        for word in line.split():
            
            word = filter(lambda x: x in string.ascii_letters, word)            
            
            if word != "":
                wordList[word] += 1
    
    f.close()
    
    
    # Write the sorted list out
    sortedWordList = sorted(wordList, key = wordList.get, reverse=True)
    
    f = open('static/mp_SimpleAliceInWonderland/out.js', 'w');
    
    f.write('var data = {\n')
    for i in range(50):
        if i > 0:
            f.write(',\n')
            
        word = sortedWordList[i]
        f.write('\t' + word + ': ' + str(wordList[word]))

    f.write('\n}')

    f.close()

      
    
    
