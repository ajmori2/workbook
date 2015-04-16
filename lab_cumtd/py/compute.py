import csv
import json
import urllib
    
def do_compute():
  url = "https://developer.cumtd.com/api/v2.2/json/GetDeparturesByStop?"
  
  urlArgs = {
    "key": "e283353ca97e4346b7ebb5e9aa3f312f",
    "stop_id": "GRGDNR"
  }
  
  req = urllib.urlopen( url + urllib.urlencode(urlArgs) )
  result = json.load( req )
  
  schedule = {}
  
  for d in result["departures"]:
    expected_mins = d["expected_mins"]
    headsign = d["headsign"]
    color = d["route"]["route_color"]
    text_color = d["route"]["route_text_color"]
    
    if headsign not in schedule:
      schedule[headsign] = { "color": color,
                             "text_color": text_color,
                             "headsign": headsign,
                             "expected": [] }
    
    schedule[headsign]["expected"].append( expected_mins )
      
  
  # Save our JSON
  f = open("res/cumtd.json", "w")
  s = json.dumps(result, indent = 4)
  f.write(s)
  
  f = open("res/schedule.json", "w")
  s = json.dumps(schedule, indent = 4)
  f.write(s)

  return 1  
