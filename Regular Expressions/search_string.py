import re

text = 'Macademia nuts, Honey tuile, Cocoa powder, Pistachio nuts'
search_pattern = re.compile('nuts')
search_match_object = search_pattern.search(text)

if search_match_object:
    print(search_match_object.span())
    print(search_match_object.start())
    print(search_match_object.end())
    print(search_match_object.group())

# Other methods of pattern
print(search_pattern.findall(text))
print(search_pattern.fullmatch('nuts'))  # The entire string must match
print(search_pattern.match('nuts...'))  # Start of the string must match
