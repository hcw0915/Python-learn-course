# TODO

while True:
  h = eval(input())
  if h == -9999 : break
  w = eval(input())
  bmi = w /((h/100)**2)
  print("BMI: %.2f" %bmi)
  
  if 30 <= bmi : print("State: fat")
  elif 25.0 <= bmi < 30 : print("State: over weight")
  elif 18.5 <= bmi < 25: print("State: normal")
  elif bmi < 18.5: print("State: under weight")	



"""
fat
over weight
normal
under weight
BMI: _
State: _
"""