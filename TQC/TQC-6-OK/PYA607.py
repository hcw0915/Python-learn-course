# TODO
n=[]
list = ["1st","2nd","3rd"]
for i in range(3):
  print("The %s student:" %(list[i]))
  for j in range(5):
    a=eval(input())
    n += [a]
  #print(n)

for j in range(3) :
  print("Student %d" %(j+1))
  print("#Sum %d" %sum(n[(j*5):(j*5+5)]))
  print("#Average %.2f" %(sum(n[(j*5):(j*5+5)])/5))
   
# sum1=sum(n[0:5])
# sum2=sum(n[5:10])
# sum2=sum(n[10:15])
# n[(j*5):(j*5+5)]  
# j=0 n[0:5] 也就是前五項的和(student 1)
# j=1 n[5:10] (student 2)
# j=2 n[10:15] (student 3)

    

"""
The _ student:
Student _
#Sum _
#Average _
"""
