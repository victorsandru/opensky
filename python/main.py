import requests
import json
from opensky_api import OpenSkyApi

api = OpenSkyApi()

#log into OpenSkyApi
data = json.load(open('items.json'))
api.__init__(data['user'],data['pass'])

planeHex = "4d229d"

s = api.get_states(0,planeHex)

print(s)