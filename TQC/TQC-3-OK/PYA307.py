# TODO
a = eval(input())

for i in range(1,a+1):
  for j in range(1,a+1):
    print("%-2d* %-2d= %-4d" %(j,i,j*i),end="")
  print()