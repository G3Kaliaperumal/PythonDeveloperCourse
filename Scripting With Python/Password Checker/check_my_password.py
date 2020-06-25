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

def get_password_leaks_count(tail_hash, hashes):
  hashes = (line.split(':') for line in hashes.splitlines())
  for h, count in hashes:
    if h == tail_hash:
      return count


def check_pwned_api(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_chars, tail = sha1password[:5], sha1password[5:]
  result = request_api_data(first5_chars)
  print(get_password_leaks_count(tail, result.text))

check_pwned_api('password123')
