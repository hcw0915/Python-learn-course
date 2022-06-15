# TODO

year = int(input())

if year % 400 == 0 :
  print("{:d} is a leap year.".format(year))
elif year % 100 == 0 :
  print("{:d} is not a leap year.".format(year))
elif year % 4 == 0 :
  print("{:d} is a leap year.".format(year))
else:
  print("{:d} is not a leap year.".format(year))

"""
_ is a leap year.
_ is not a leap year.
"""