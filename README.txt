Geocoders
=========

Code for accessing various geocoding web services with an ultra simple API:

    name, (lat, lon) = geocode('london')

The geocode functions return (unicode_place_name, (float_lat, float_lon)) if
the string can be geocoded, and (None, (None, None)) if it cannot.

Currently supported: Google Geocoder, Yahoo! Geocoder, and Yahoo! Placemaker.

Google:

>>> from geocoders.google import geocoder
>>> geocode = geocoder('GOOGLE-API-KEY')
>>> geocode('new york')
(u'New York, NY, USA', (-73.986951000000005, 40.756053999999999))
>>> geocode('oneuth')
(u'South, Bloomfield, NY 14469, USA', (-77.5385449999999, 42.865267000000003))

Yahoo:

>>> from geocoders.yahoo import geocoder
>>> geocode = geocoder('YAHOO-API-KEY')
>>> geocode('new york')
(u'New York, NY, US', (40.714550000000003, -74.007124000000005))
>>> geocode('oneuth')
(u'Aneth, UT 84510, US', (37.217799999999997, -109.189911))

Yahoo! Placemaker:

>>> from geocoders.placemaker import geocoder
>>> geocode = geocoder('YAHOO-API-KEY')
>>> geocode('new york')
(u'New York, NY, US', (40.714500000000001, -74.007099999999994))
>>> geocode('oneuth')
(None, (None, None))

While Yahoo! Placemaker isn't strictly designed as a geocoder, in practice it
can be useful for things like "did you mean location X" in a regular search
engine.
