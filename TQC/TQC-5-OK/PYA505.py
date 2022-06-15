# TODO

a = input()
x = eval(input())
y = eval(input())

def compute(a,x,y):
  for i in range(y):
    for j in range(x):
      print("%-2s" %a , end="")
    print('')
compute(a,x,y)
    
