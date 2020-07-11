DATA_MAX_SIZE = 100000000
length = 10000000000
num, lef = divmod(length, DATA_MAX_SIZE)  # Return the tuple (x//y, x%y).  Invariant: div*y + mod == x.
print num, lef
