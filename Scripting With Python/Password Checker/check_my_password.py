# SHA1 Hash Generator
# https://passwordsgenerator.net/sha1-hash-generator/

import requests
import hashlib
import sys


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
            return int(count)
    return 0


def check_pwned_api(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_chars, tail = sha1password[:5], sha1password[5:]
    result = request_api_data(first5_chars)
    return get_password_leaks_count(tail, result.text)


def main(args):
    for password in args:
        count = check_pwned_api(password)
        if count > 0:
            print(f'Your password {password} was found {count} times.. You should try changing your password.')
        else:
            print(f'Great!! Your password {password} is not hacked')


if __name__ == '__main__':
    with open('Passwords.txt', 'r') as input_file:
        inputs = input_file.read().splitlines()
        main(inputs)
