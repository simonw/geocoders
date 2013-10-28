import urllib
from utils import simplejson, geocoder_factory

# https://developers.google.com/maps/documentation/geocoding/


def geocode(q, api_key=None):
    json = simplejson.load(urllib.urlopen(
        'http://maps.googleapis.com/maps/api/geocode/json?' + urllib.urlencode({
            'address': q,
            'sensor': 'false',
        })
    ))
    try:
        lon = json['results'][0]['geometry']['location']['lng']
        lat = json['results'][0]['geometry']['location']['lat']
    except (KeyError, IndexError):
        return None, (None, None)
    name = json['results'][0]['formatted_address']
    return name, (lat, lon)

geocoder = geocoder_factory(geocode)
