# list comprehension
for i in [x*3 for x in [1, 2, 3, 4, 5]]:
    print(i)

print()

# this isn't a "tuple comprehension"
# a generator
# the generator and the listcomp produce the same data
# BUT they do not execute in the same way!!!
for i in (x*3 for x in [1, 2, 3, 4, 5]):
    print(i)