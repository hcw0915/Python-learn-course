# TODO
x = []
for i in range(1,11):
  a = input()
  x += [a]
  list_x = [int(i) for i in x]  
w = sorted(list_x)
print(w[0])





"""
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