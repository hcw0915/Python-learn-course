"""
  # Exercise.1 - 變數計算
a = 4
b = 6
c = a + b 
d = a * b
print(c)
print(d)

a = "3"
b = "5"
c = a + b
print(c)

  # Exercise.2 - 字串連結
name = "Antonio"
addr = "Taipei"
age = 29
info = name + addr + str(age)
print(info)

  # Exercise.3 - 字串+變數聯結
age = "23"
info = "I'm" + age + "years old"
print(info)

  # Exercise.4 - 斷行處理(\n)
print("ABC\nDEF\n123\n456")

  # Exercise.5 - 認識型別(int、str float)
price = 400
print(type(price))

a = 400000.232
print(type(a))

b = "-1234123"
print(type(b))

  # Exercise.6 - 型別轉換(int、str float)
a = 1
print(type(a))
b = "2" 
print(type(b))
c = 3.4
print(type(c))

x = str(a)
print(type(x))
y = int(b)
print(type(y))
z = int(c)
print(type(z))

q = float("5.6")
print(q)
p = float(65)
print(p)
w = str(22)
print(w)
e = str("6.5")
print(e)

a = "3"
b = 5
c = int(a) + b
print(c)

age = 29
info =  "I'M " + str(age) +" years old."
print(info)


age = 10
mystr = "hello"
print(age,mystr)

  # Exercise.7 - input應用
age = input("請輸入年齡:")
print("I'M " + age +" years old.")
"""

object = input("請輸入品名:")
price = input("請輸入單價:")
num = input("請輸入數量:")
total = int(price) * int(num)
print("您購買的是",object,"，單價為",price,"元，數量為",num,"個，總價為",total,"元。")