# TODO

def compute(row,cols):
  for i in range(row):
    for j in range(cols):
      print("%4d"%(j-i),end="") 
      
    print("") #每次j列跑完就換行 

row = eval(input())
cols = eval(input())
compute(row,cols)
    

