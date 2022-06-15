# TODO


count = eval(input())
i = 0
while i < count:
  num = input()
  x=[]
  for a in num:
    x += [a]
    int_list = [int(i) for i in x]
    total = sum(int_list)
  print("Sum of all digits of %s is %d" %(num,total))
  i += 1



"""
Sum of all digits of _ is _
"""