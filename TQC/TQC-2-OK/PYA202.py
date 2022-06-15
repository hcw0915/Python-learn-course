# TODO


a = eval(input())
x = a % 3
y = a % 5
if (x == 0) and (y == 0):
  print("{:d} is a multiple of 3 and 5.".format(a))
elif (x == 0) and (y != 0):
  print("{:d} is a multiple of 3.".format(a))
elif (x != 0) and (y == 0):
  print("{:d} is a multiple of 5.".format(a))
else:
  print("{:d} is not a multiple of 3 or 5.".format(a))

"""
_ is a multiple of 3 and 5.
_ is a multiple of 3.
_ is a multiple of 5.
_ is not a multiple of 3 or 5.
"""