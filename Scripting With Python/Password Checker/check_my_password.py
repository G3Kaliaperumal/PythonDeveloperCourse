# SHA1 Hash Generator
# https://passwordsgenerator.net/sha1-hash-generator/

import requests
import hashlib


def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching the response. Status: {res.status_code}. Please check the api and try again')
  return res


def check_pwned_api(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  result = request_api_data(sha1password[0:5])
  print(result)


check_pwned_api('password123')

