side1 = eval(input())
side2 = eval(input())
side3 = eval(input())

#TODO
sum = side1 + side2 + side3

if side1 >= side2 and side1 >= side3 and side1 < side2 + side3:
  print(sum)
elif side2 >= side1 and side2 >= side3 and side2 < side1 + side3:
  print(sum)
elif side3 >= side2 and side3 >= side1 and side3 < side2 + side1:
  print(sum)
else:
  print("Invalid")


"""
Invalid
"""