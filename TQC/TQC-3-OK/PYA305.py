# TODO

a = input()
x = len(a)-1

if (a != 0):
  for i in range(x,-1,-1):
    print(a[i],end="")
else:
  print(a)