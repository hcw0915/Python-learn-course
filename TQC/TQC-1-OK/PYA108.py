# TODO

x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())

dis = (pow(x1-x2,2)+pow(y1-y2,2)) ** 0.5
print("(",x1,",",y1,")")
print("(",x2,",",y2,")")
print("Distance = {:.4f}".format(dis))
