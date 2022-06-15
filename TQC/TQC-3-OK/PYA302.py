# TODO
a = eval(input())
b = eval(input())


if a % 2 == 1 :
  if b % 2 == 1 :
    c = 0
    for i in range(a+1,b,2):
      c += i
    print(c)
  else:
    c = 0
    for i in range(a+1,b+1,2):
      c += i
    print(c)
elif a % 2 == 0 :
  if b % 2 == 1 :
    c = 0
    for i in range(a,b,2):
      c += i
    print(c)
  else:
    c = 0
    for i in range(a,b+1,2):
      c += i
    print(c)
    
  