nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def generator(nested_list):
    for i in nested_list:
        for y in i:
            yield y

for item in generator(nested_list):
    print(item)