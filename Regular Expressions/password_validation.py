import re

password_regex = re.compile(
    r'(^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#$%@]))[a-zA-Z\d#$%@]{8,15}$')
password = input('Enter Password: ')

while(not password):
    password = input('Enter Password: ')

is_password_valid = password_regex.search(password)
print('Valid password') if is_password_valid else print(
    'Invalid password! Pwd should have 8 to 15 characters and should contain atleast 1 lowercase letter, 1 uppercase letter, 1 number and 1 special character($ or @ or # or %)')
