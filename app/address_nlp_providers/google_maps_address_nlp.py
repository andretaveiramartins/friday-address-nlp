from requests import get
from pprint import pprint
from json import dump
from csv import QUOTE_ALL, DictWriter
from .. import Utils
import yaml
import os

try:
    config = Utils.load_yml_config(os.path.join("config.yml"))
except yaml.YAMLError as exc:
    print (exc)

API_KEY = config['google_api_key']

def _address_resolver(json):
    final = {}
    if json['results']:
        data = json['results'][0]
        for item in data['address_components']:
            for category in item['types']:
                data[category] = {}
                data[category] = item['long_name']
        final['street'] = data.get("route", None)
        final['state'] = data.get("administrative_area_level_1", None)
        final['city'] = data.get("locality", None)
        final['county'] = data.get("administrative_area_level_2", None)
        final['country'] = data.get("country", None)
        final['postal_code'] = data.get("postal_code", None)
        final['neighborhood'] = data.get("neighborhood",None)
        final['sublocality'] = data.get("sublocality", None)
        final['housenumber'] = data.get("housenumber", None)
        final['postal_town'] = data.get("postal_town", None)
        final['subpremise'] = data.get("subpremise", None)
        final['latitude'] = data.get("geometry", {}).get("location", {}).get("lat", None)
        final['longitude'] = data.get("geometry", {}).get("location", {}).get("lng", None)
        final['location_type'] = data.get("geometry", {}).get("location_type", None)
        final['postal_code_suffix'] = data.get("postal_code_suffix", None)
        final['street_number'] = data.get('street_number', None)
    return final
    
def process_address(address):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?components=&language=&region=&bounds=&key='+API_KEY
    url = url + '&address='+ address.replace(" ","+")
    data= None
    try:
        pass
    except Exception as identifier:
        pass
    response = get(url)
    response.raise_for_status()
    data  = _address_resolver(response.json())
    data['address'] = address
    return data
