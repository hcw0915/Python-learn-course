# def

"""
def fun_1(name="cherry",age = "50",a=100,b=100):
  print("我是",name,"hello."); #記得要有;分號
  print(age);
  print(a);
  print(b);
  total = a + b
  print(total);

name = "Anna" #可設定變數
age = "26"
a = 100 
b = 456
fun_1(name,34,6,8)  #將變數帶入function def中 依順序處理
fun_1("Antonio",40,2,4)
fun_1("Bob",30,4,78)
fun_1(name,age,a,b) #未設定變數，帶入預設值

"""
 #小實作 

"""

def order(num ="A"):  #若為非正確輸入，則預設為A套餐
  dic = {"1":"A","2":"B","3":"C"} # 用dictionary 做1=A 2=B 3=C 的設定
  print("你點的是",dic[num],"套餐")

  #可用if替換
  #if num == 1 : num = "A"
  #elif num == 2 : num = "B"
  #elif num == 3 : num = "C"
  #else: None  #回預設值
  #print("你點的是",num,"套餐");

num = input("請輸入你要的餐點:\
  \n1.A套餐:漢堡+奶茶 100元\
  \n2.B套餐:薯條+紅茶 130元\
  \n3.C套餐:漢堡+薯條+可樂 150元\n") # "\"尾部斜線是整理code換行用，不顯示；"\n"頭部，表是執行端換行
order(num)

#-----------------------------------------------------------------------
from sys import exit

def func(name,gender):
  dic_2 = {"1":"先生","2":"小姐"}
  print(name,dic_2[gender],"你好");
  
name = input("請輸入姓名:\n")
gender = input("請輸入性別 1.先生 2.小姐:\n")
if gender == "1" or gender == "2": #-if段-是為了避免輸入錯誤的狀況
  None
else:
  print("輸入錯誤，請重新執行程式")
  exit()
func(name,gender)


#-----------------------------------------------------------------------
# Return

def fn(x):
  return x**2;

def fn_2(x):
  x=x+5;
  return x; 

w = eval(input())
print(fn(w))
print(fn_2(w))

"""


def fn_3(a,b):
  c = a + b
  return c;

print("共",fn_3(3,4),"元")



