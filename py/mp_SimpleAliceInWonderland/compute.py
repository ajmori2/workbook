
def do_compute():
    f = open('../static/mp_SimpleAliceInWonderland/AliceInWonderland.txt', 'r');
    
    # Count the times each word appears in Alice in Wonderland
    wordList = {}
    
    for line in f:
        for word in line.split():
            wordList[word] += 1
    
    
    f = open('../static/mp_SimpleAliceInWonderland/out.json', 'w');
    
    # Write the sorted list out
    for word in sorted(wordList, key = wordList.get, reverse=True):
            f.write(word);
    
