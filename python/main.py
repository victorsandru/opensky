import requests
import json
from opensky_api import OpenSkyApi

api = OpenSkyApi()

#log into OpenSkyApi
data = json.load(open('items.json'))
api.__init__(data['user'],data['pass'])

planeHex = "3c4b23"

s = api.get_states(0,planeHex)
states = s.__dict__['states'][0].__dict__


# print(s)
print(states['origin_country'])
print("long: " + str(states['longitude']) + "\nlat: " + str(states['latitude']))