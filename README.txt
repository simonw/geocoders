Geocoders
=========

Code for accessing various geocoding web services with an ultra simple API:

    name, (lat, lon) = geocode('london')

Currently supported: Google Geocoder, Yahoo! Placemaker

Google:

>>> from geocoders.google import geocoder
>>> geocode = geocoder('GOOGLE-API-KEY')
>>> geocode('new york')
(u'New York, NY, USA', (-73.986951000000005, 40.756053999999999))
>>> geocode('oneuth')
(u'South, Bloomfield, NY 14469, USA', (-77.5385449999999, 42.865267000000003))

Yahoo! Placemaker:

>>> from geocoders.placemaker import geocoder
>>> geocode = geocoder('YAHOO-API-KEY')
>>> geocode('new york')
(u'New York, NY, US', (40.714500000000001, -74.007099999999994))
>>> geocode('oneuth')
(None, (None, None))

The geocode functions return (unicode_place_name, (float_lat, float_lon)) if
the string can be geocoded, and (None, (None, None)) if it cannot.
