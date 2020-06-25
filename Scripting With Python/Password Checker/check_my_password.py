# SHA1 Hash Generator
# https://passwordsgenerator.net/sha1-hash-generator/

import requests

url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
res = requests.get(url)
print(res)
