import requests, time
r = requests.post('http://challenge01.root-me.org/web-client/ch18/', data={"message":"1111111111111111111", "titre":"dddd"})
print r.status_code
print r.content