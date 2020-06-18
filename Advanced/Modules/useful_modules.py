from collections import Counter, defaultdict, OrderedDict

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
