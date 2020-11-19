from urllib.request import urlopen

try:
    urlopen('http://google.com')
    i = urlopen('http://google.com')
except Exception:
    i = None
finally:
    if i == None:
        print('False')
    else:
        print('True')