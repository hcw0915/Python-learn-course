# TODO
a = eval(input())
b = eval(input())
c = eval(input())

def compute(a,b,c):
  d = (-b + (b*b-(4*a*c))**0.5)/(2*a)
  D = (-b - (b*b-(4*a*c))**0.5)/(2*a)
  if type(d) != float or type(D) != float:
    print("Your equation has no root.")
  elif d == D:
    print("%.1f" %(d))
  else:
    print("%.1f, %.1f" %(d,D))
  
compute(a,b,c)


"""
Your equation has no root.
"""