# Important links:
# https://regex101.com
import re

# r'([a-z]) ([0-9])' => Explanation below
# r => indicates the python compiler that it is a regular expression
# [a-z] => matches a character between a to z
# [0-9] => matches a character between 0 to 9
# Thus, the given regular expressions matches a string with a character, space and a number
# Examples: a 0 || v 9 || h 8
regex_expression = re.compile(r'([a-z]) ([0-9])')
test_string = 'Regex 1010'
search_result = regex_expression.search(test_string)
print(search_result.group())
