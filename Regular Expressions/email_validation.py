
import re

regex_expression = re.compile(
    r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')
test_string = 'a@a.com'
search_result = regex_expression.search(test_string)
if search_result:
    print('Valid email address')
else:
    print('Invalid email address')
