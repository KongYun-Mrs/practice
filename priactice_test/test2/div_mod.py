DATA_MAX_SIZE = 100000000
length = 10000000000
num, left = divmod(length, DATA_MAX_SIZE)  # Return the tuple (x//y, x%y).  Invariant: div*y + mod == x.
print(num, left)
