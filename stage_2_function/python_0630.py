import pymysql
conn = pymysql.connect(host='localhost',user='root',passwd='',db='python',charset='utf8')
cur = conn.cursor() 
print("Success")

def myindex():
  print("管理者登入系統")
  print("*------------*")
  print("1.登入")
  print("2.註冊帳號")
  print("3.結束程式")

def myindex2():
  print("請選擇以下動作")
  print("*------------*")
  print("1.查詢所有員工的資料")
  print("11.查詢員工的資料")
  print("2.修改員工資料")
  print("3.刪除員工帳號")
  print("4.離開")

def mymenu():
  while True:
    myindex()
    num = int(input("請輸入你要執行的動作"))
    if num == 1:
      print("Log in!")
    elif num == 2:
      print("Register")
    elif num == 3:
      print("Exit!")
      break

myindex()
myindex2()

cur.close()
conn.close()
print("Log out!!")