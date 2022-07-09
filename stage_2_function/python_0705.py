import pymysql
conn = pymysql.connect(host='localhost',user='root',passwd='',db='python',charset='utf8')
cur = conn.cursor() 
print("MySQL-DataBase Connection-Successful.")

def Managers_login_interface():
  print("管理者登入系統")
  print("*------------*")
  print("1.登入")
  print("2.註冊帳號")
  print("3.結束程式")

def Managers_login_list():
  while True:
    Managers_login_interface()
    num = int(input("請輸入你要執行的動作:"))
    if num == 1:
      print("Success!")
      staff_data_query()
    elif num == 2:
      print("Register")
      staff_data_insert()
    elif num == 3:
      print("Exit!")
      break

def Operating_interface():
  print("請選擇以下動作")
  print("*------------*")
  print("1.查詢所有員工的資料")
  print("11.查詢員工的資料")
  print("2.修改員工資料")
  print("3.刪除員工帳號")
  print("4.離開")
  while True:
    a = input("請輸入你要執行的動作:")
    if a == "1":
      print("你選擇的是查詢所有員工資料")
    elif a == "11":
      print("你選擇的是查詢員工資料")
    elif a == "2":
      print("你選擇的是修改員工資料")
    elif a == "3":
      print("你選擇的是刪除員工帳號")
    elif a == "4":
      print("你已離開本系統，返回登入頁面")
      break

def Operating_list():
  while True:
    Operating_interface()
    item = int(input("請輸入您執行的行動:"))
    if item == 1 :
      print("查詢所有資料")
    elif item == 2 :
      print("更新資料")
    elif item == 3 :
      print("刪除資料")
    elif item == 4 :
      break

def staff_data_query():  # 還要再修正登入系統
  while True: 
    # 從SQL裡面抓資料
    user_acc = input("請輸入帳號:")

    if user_acc == "" : 
      print("你輸入為空值，請重新執行。")
      break

    sql_1 = "SELECT sf_name,sf_account,sf_pwd FROM staff_info WHERE sf_account='"+user_acc+"' AND sf_del = '0'" 
    cur.execute(sql_1) # 資料庫執行抓資料存在cur裡  # sql 裡面抓變數用"+變數+"
    staff_info = cur.fetchone() # print(staff_acc) # 總共抓了 名字、帳號、密碼三個欄位
  
    if staff_info == None: 
      print("此帳號不存在")
      continue

    staff_pwd = staff_info[2]
    user_pwd = input("請輸入密碼:")
    if user_pwd == "":
      break
    if staff_pwd == user_pwd:
      print("登入成功")
      Operating_list()
      break
    else:
      print("密碼錯誤")
      continue

def staff_data_insert():
  while True:
    name = input("請輸入姓名:")
    if name == "" :
      print("姓名不能為空")
      continue

    acc=input("請輸入帳號")
    if acc == "" :
        print("帳號不能為空")
        continue

    sql = "SELECT * FROM staff_info WHERE sf_account = '"+ acc + "'"
    cur.execute(sql)
    data = cur.fetchone()

    if not data == None:
        print("{}帳號已存在".format(acc))
        continue
    pwd = input("請輸入密碼")
    sql_insert = "INSERT INTO staff_info(sf_name,sf_account,sf_pwd,create_user,update_user)VALUES('"+name+"','"+acc+"','"+pwd+"','"+name+"','"+name+"')" 
    #print(sql_insert)
    cur.execute(sql_insert)
    conn.commit() 
    print("使用者 {} :帳號已註冊成功，可以重新登入已進入系統".format(acc))
    break

def staff_data_update():
  sql_1 = "SELECT sf_name,sf_account,sf_pwd FROM staff_info WHERE sf_account='"+user_acc+"' AND sf_del = '0'" 
  cur.execute(sql_1) # 資料庫執行抓資料存在cur裡  # sql 裡面抓變數用"+變數+"
  staff_info = cur.fetchone() # print(staff_acc) # 總共抓了 名字、帳號、密碼三個欄位


  return None

def staff_data_delete():
  return None

# Managers_login_interface()
# Operating_interface()


Managers_login_list()


cur.close()   # 關閉資料庫
conn.close()  # 關閉連線
print("資料庫關閉成功") # 確認有完成關閉
