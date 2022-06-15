# TODO


while True:
  year = eval(input())
  if year == -9999 : break
  
  if year % 400 == 0 : print("%d is a leap year." %year)
  elif year % 100 == 0 : print("%d is not a leap year." %year)
  elif year % 4 ==0 : print("%d is a leap year." %year)
  else: print("%d is not a leap year." %year)


"""
_ is a leap year.
_ is not a leap year.
"""
