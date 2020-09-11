vowels = {'a', 'e', 'i', 'o', 'u'}
message = "Hello I'm Hieu"

""" found = set()
for v in vowels:
    if v in message:
        found.add(v) """
found = {v for v in vowels if v in message}

print(found)