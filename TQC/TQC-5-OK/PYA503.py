# TODO

a = eval(input())
b = eval(input())

def compute(a,b):
  c = 0
  for i in range(a,b+1):
    c += i 
  print(c)
    
compute(a,b)