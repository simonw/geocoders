# Yuck! http://code.activestate.com/recipes/475126/
try:
    import xml.etree.ElementTree as ET # in python >=2.5
except ImportError:
    try:
        import cElementTree as ET # effbot's C module
    except ImportError:
        try:
            import elementtree.ElementTree as ET # effbot's pure Python module
        except ImportError:
            import lxml.etree as ET # ElementTree API using libxml2

try:
    import json as simplejson
except ImportError:
    import simplejson

# Methods for helping with namespace handling in ElementTree
def make_nsfind(nsdict=None):
    nsdict = nsdict or {}
    def find(et, xpath):
        xpath = fix_ns(xpath, nsdict)
        return et.find(xpath)
    return find

def make_nsfindall(nsdict=None):
    nsdict = nsdict or {}
    def find(et, xpath):
        return et.findall(fix_ns(xpath, nsdict))
    return find

def fix_ns(xpath, nsdict=None):
    nsdict = nsdict or {}
    for ns, url in nsdict.items():
        xpath = xpath.replace('%s:' % ns, '{%s}' % url)
    return xpath

def partial2(fn):
    def inner1(arg2):
        def inner2(arg1):
            return fn(arg1, arg2)
        return inner2
    return inner1

