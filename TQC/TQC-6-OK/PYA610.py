#TODO
n = []
for i in range(4):
  print("Week %d:" %(i+1))
  for j in range(3):
    print("Day %d:" %(j+1),end="")
    degree = eval(input())
    n.append(degree)

print("Average: %.2f" %(sum(n)/len(n)))
print("Highest: {}" .format(max(n)))
print("Lowest: {}" .format(min(n)))

"""
Week _:
Day _: 
Average: _
Highest: _
Lowest: _
"""