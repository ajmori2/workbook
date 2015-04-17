import csv
import json
import urllib
    
def do_compute():
  # Grab your CUMTD key from ../static/keys/cumtd.txt
  # ...raise an error if the key file is empty
  f = open("../static/keys/cumtd.txt")
  cumtd_key = f.read().strip()

  if len(cumtd_key) == 0:
    raise ValueError("No CUMTD API key provided in /static/keys/cumtd.txt")
  

  # Prepare the API request
  url = "https://developer.cumtd.com/api/v2.2/json/GetDeparturesByStop?"
  
  urlArgs = {
    "key": cumtd_key,
    "stop_id": "GRGDNR"
  }


  # Make the API request and store the result JSON in `result`  
  req = urllib.urlopen( url + urllib.urlencode(urlArgs) )
  result = json.load( req )
  
  
  # Parse result into a `schedule` dictionary to be used by JavaScript
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
  # ...first the full `result` (for debugging)
  f = open("res/cumtd.json", "w")
  s = json.dumps(result, indent = 4)
  f.write(s)
  
  # ...and also the `schedule` (for our JavaScript to use)
  f = open("res/schedule.json", "w")
  s = json.dumps(schedule, indent = 4)
  f.write(s)

  return 1  
