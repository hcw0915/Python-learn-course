# TODO

n = eval(input())

total = 0
for i in range(2,n+1):
  sum = 1 / ((i-1)**0.5 + i**0.5)
  total += sum
print("%.4f" %total)  
