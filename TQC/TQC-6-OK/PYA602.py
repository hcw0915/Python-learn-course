# TODO
a = []
i = 0
while i < 5 :
  n = input()
  if n == "J" : n = "11"
  elif n == "Q" : n = "12"
  elif n == "K" : n = "13"
  elif n == "A" : n = "1"
  a = a + [n]
  i += 1

list_int_a = [int(i) for i in a ]
total = sum(list_int_a)
print(total)