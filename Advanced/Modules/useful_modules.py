from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array

sentence = "Hello"
print(Counter(sentence))

# defaultdict helps to generate a default value if the given key does not exists in the dictionary
dict1 = defaultdict(lambda: 10, {
    'a': 1,
    'b': 2
})
print(dict1['c'])

# Order of the key, value pair is maintained in OrderDict
dict2 = OrderedDict({
    'a': 1,
    'b': 2
})

dict3 = OrderedDict({
    'b': 2,
    'a': 1
})
print(dict2 == dict3)

print(datetime.time(11, 57, 2))
print(datetime.date.today())

arr = array('i', [1, 2, 3])
print(arr[0])
