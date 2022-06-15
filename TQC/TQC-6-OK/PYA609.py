#TODO
a=[[],[]]
b=[[],[]]
print("Enter matrix 1:")
#TODO
for i in range(2):
        for j in range(2):
        #置於迴圈內，依給定之格式輸出
                print("[%d, %d]: " % (i+1, j+1), end = '')
                num=eval(input())
                a[i].append(num)
print("Enter matrix 2:")
#TODO
for i in range(2):
        for j in range(2):  
        #置於迴圈內，依給定之格式輸出
                print("[%d, %d]: " % (i+1, j+1), 
                      )
                num=eval(input())
                b[i].append(num)
print("Matrix 1:")
#TODO
for i in range(2):
        for j in range(2):
                print("%d" % (a[i][j]),end=" ")
        print("")
print("Matrix 2:")
#TODO
for i in range(2):
        for j in range(2):
                print("%d" % (b[i][j]),end=" ")
        print("")
print("Sum of 2 matrices:")
#TODO
for i in range(2):
        for j in range(2):
                print("%d" % (a[i][j]+b[i][j]),end=" ")
        print("")
