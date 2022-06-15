# TODO
num = eval(input())
for i in range(1,num+1): 
  for j in range(1,i+1): 
    x = i*j
    print("%4d" %x, end="") 
  print("")
  