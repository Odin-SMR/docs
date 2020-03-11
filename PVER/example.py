# Setup the name space:
import requests

# Start by making a request to the root URI of the DDS API:
r0 = requests.get('http://odin.rss.chalmers.se/rest_api/v5/level2/DDS/')

# The request contains the returned JSON object, which in Python is a
# dictionary, which can be printed or inspected to find out its keys and
# contents.  Let's assume that we have done that, or that we have read
# the API documentation, so that we know that 'FreqMode' is a key.
# Use this to single out the frequency mode of interest, in this case 2:
FM2 = [x for x in r0.json()['Data'] if x['FreqMode'] == 2][0]

# Make a new request using the URI provided in the JSON object:
r1 = requests.get(FM2["URLS"]["URL-scans"])

# Filter out data from 2012-03-11 and fetch the level2 data for the
# first scan in the list:
day = [x for x in r1.json()['Data'] if x['Date'] == '2012-03-11']
r2 = requests.get(day[0]['URLS']['URL-level2'])

# The Level2 data available to us, along with the ancillary and
# auxilliary data:

L2 = r2.json()['Data']['L2']
L2anc = r2.json()['Data']['L2anc']
L2aux = r2.json()['Data']['L2i']

# Now we have the data at hand and can proceed with crunching it!
