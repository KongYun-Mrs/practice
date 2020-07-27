import re

a = [1, 2, 3, 4, 5, '<65', '>12']
a = str(a)
a = a.strip("[").strip("]")
print a
s1 = re.match("^\d+.+?(\'<\d+\').+?(\'>\d+\')", a)
print s1.group(1)

# print s1.group(0)
