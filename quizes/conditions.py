# Let's see what Python gives us when we check some conditions. This is very helpful to know,
# when it comes to if or while statements

a = []      # is an empty list
b = None    # is None
c = [{}]    # is an empty dict in a list
d = {}      # is just an empty dict
bool_list = [True, True, False, True]
# some_dict = {'a': 'str1', 'b':5, 'c': False, 'd':None}
some_dict = dict(a='str1', b=5, c=False, d=None)


# let's test

if len(a) == len(c):
    print('a and c has same length')
else:
    print('length a is', len(a))
    print('length c is', len(c))

if a:
    print("Python means that a is 'true' ")
elif a is None: # or a == None
    print("Python means that a is 'None'-type ")
elif a == [] and not a:
    print('Python says that a is an empty list,\nand that if not a == True')
else:
    print('What else cound a be then?')

if b:
    "Python means that 'if b' is true'"
elif not b and b is None:
    'so b is not and b is None, too.'

if isinstance(a, list) and isinstance(c, list):
    print('a is a list')

for i in range(len(bool_list)):
    if bool_list[i]:
        print("index {} of bool_list is true".format(i))


# Following three times the same output but written differently

# get the value by from dictionary inside the loop with dict[key]
for k in some_dict.keys():
    print("key: {} / val: {}".format(k, some_dict[k]))

# get a tuple (key, value) for each item in the dict
for key, value in some_dict.items():
    print("key: {} / val: {}".format(key, value))

# if you want to iterate of as many lists as you want using zip()
keys = [*some_dict.keys()]
vals = [*some_dict.values()]

for key, value in zip(keys, vals):
    print("key: {} / val: {}".format(key, value))

