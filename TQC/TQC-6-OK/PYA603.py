# TODO

# a = []
# i = 0
# while i < 10:
#   n = input()
#   a = a + [n]
#   i = i + 1
# list_int_a = [int(j) for j in a]
# list_int_a.sort()
# print(a[-1],a[-2],a[-3])
  
a = []
for i in range(10):
  a.append(eval(input()))
a.sort()
print(a[-1],a[-2],a[-3])