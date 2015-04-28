import json
import urllib
from itertools import permutations
from collections import defaultdict

def buildMatrix(gmapsResult):
    cities = gmapsResult['origin_addresses']
    table = defaultdict(dict)
    for i,origin in enumerate(cities):
        for j,destination in enumerate(cities):
            table[origin][destination]=gmapsResult['rows'][i]['elements'][j]['duration']['value']
    return cities, table

def computeDist(r,distMatrix):
    sum = 0
    for i in range(len(r)):
        sum += distMatrix[r[i]][r[(i+1)%len(r)]] #distance from r[i] to r[i+1]
    return sum

def bestRoute(cities,distMatrix):
    minDist = computeDist(cities,distMatrix)#keeps track of least distance so far
    minRoute = cities #keeps track of best route so far
    for c in permutations(cities[1:]):
        route = (cities[0],) + c
        dist = computeDist(route,distMatrix)
        if dist < minDist:
            minDist = dist
            minRoute = route
    return minRoute
    
def do_compute():

    #cities_seed = ["columbus, oh","ohiopyle","las vegas, nv","yellowstone","yosemite CA"]
    cities_seed = ["Chicago, IL","new york city, NY","atlanta, ga","los angeles, CA","curtis, ne","seattle, wa", "san jose, ca"]
    cities_str = '|'.join(cities_seed)

    url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={0}&mode=driving&language=en-EN".format(cities_str)
    result = json.load(urllib.urlopen(url))
    cities,distMatrix = buildMatrix(result)
    minRoute = tuple(bestRoute(cities,distMatrix))
    #minRoute = tuple(cities)

    output = {'route': minRoute + (minRoute[0],)}

    # Save our JSON
    f = open("res/data.json", "w")
    s = json.dumps(output, indent = 4)
    f.write(s)

    return 1  
