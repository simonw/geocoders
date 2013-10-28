import urllib
from utils import simplejson, geocoder_factory

def geocode(q, email):
    """
    Geocode a location query using OpenStreetMap's Nominatim API.
    Pass an email address, as a courteous gesture, to allow the OSM
    admins to contact you if you are using too many resources.

    """

    json = simplejson.load(urllib.urlopen(
        'http://nominatim.openstreetmap.org/search?' + urllib.urlencode({
            'q': q,
            'format': 'json',
            'email': email
        })
    ))
    try:
        lon, lat = json[0]['lon'], json[0]['lat']
    except (KeyError, IndexError):
        return None, (None, None)
    name = json[0]['display_name']
    return name, (lat, lon)

geocoder = geocoder_factory(geocode)
