from sys import exit
import random

user_acc = 123
user_pwd = 321

print("------------------------")
print("------python小程式------")
print("------------------------")

for i in range(1,4,1):
  acc = eval(input("請輸入帳號:"))
  pwd = eval(input("請輸入密碼:"))
  if (user_acc == acc) and (user_pwd == pwd) :
    print("帳號輸入正確，登入成功\n")
    break
  else:
    print("帳號或密碼輸入錯誤",i,"次，剩餘",3-i,"次機會")
    if i == 3:
      print("帳號已鎖定，請洽管理員。")
      exit()
while True:
  print("請選擇你想要執行的程式(請輸入1-4):\n1.BMI計算\n2.溫度換算\n3.公里/英哩轉換\n4.結帳系統\
        \n5.九九乘法表\n6.終極密碼\n7.小遊戲-PY升職記\n8.數字AB遊戲\n9.PY_21點\n0.離開")
  choose = eval(input())

    #--------離開程式--------#
  if choose == 0 :
    check = (input("請問是否確認離開程式(Y/N)"))
    if check == "Y":
      print("你已離開程式!!!!")
      exit()
    else:
      None
          
    #--------BMI計算--------#  
  elif choose == 1 :
    print("歡迎來到PY健康中心")
    name = input("請輸入姓名:")
    weight = eval(input("請輸入體重(kg):"))
    height = eval(input("請輸入身高(cm):")) / 100
    bmi = weight / pow(height,2) #bmi = weight / (height ** 2)
    print("{:s},你好,你的BMI為{:.1f}(kg/cm2)".format(name,bmi))
    
    #--------溫度換算--------#
  elif choose == 2 :
    print("歡迎來到PY溫度計")
    print("請輸入你要傳換的溫度單位(1/2):\n1.華式\n2.攝氏")
    option = eval(input())
    if option == 1:
      cel = input("請輸入攝氏溫度:")
      fah = ( float(cel) * 9 / 5 ) + 32
      print("現在溫度為華氏{:.2f}度。".format(fah))
    elif option == 2:
      fah_2 = input("請輸入華氏溫度:")
      cel_2 = ( float(fah_2) - 32 ) * 5 / 9
      print("現在溫度為攝氏{:.2f}度。".format(cel_2))
    elif option == "":
      print("輸入錯誤，系統回覆為空值!")
    else:
      print("輸入錯誤!")
    
    #--------公/英里換算--------#
  elif choose == 3 :
    print("歡迎來到PY公/英哩傳換器")
    print("請輸入你要兌換的長度單位(1/2):\n1.公里\n2.英哩")
    print("(目前公里/英哩為 1 km:0.6 miles)")
    num = eval(input())
    
    if num == 1:
      km = eval(input("請輸入公里數:")) 
      miles = km * 0.62
      print("{:.2f}公里為{:.2f}英哩。".format(km,miles))
    elif num == 2:
      miles = eval(input("請輸入英哩數:")) 
      km = miles / 0.6
      print("{:.2f}英哩為{:.2f}公里。".format(miles,km))
    elif num == "":
      print("輸入錯誤，系統回覆為空值!")
    else:
      print("輸入錯誤!")
    
    #--------飲料店結帳--------#
  elif choose == 4 :
    print("歡迎來到PY飲料店")
    cola = 25
    milk_tea = 35
    green_tea = 20
    print("可樂{:d}元、奶茶{:d}元、綠茶{:d}元".format(cola,milk_tea,green_tea))
    #初始
    total = 0
    print("目前金額為",total,"元")
    #可樂
    num_1 = eval(input("請輸入可樂數量:"))
    total += cola * num_1
    print("目前金額為",total,"元")
    #奶茶
    num_2 = eval(input("請輸入奶茶數量:"))
    total += milk_tea * num_2
    print("目前金額為",total,"元")
    #綠茶
    num_3 = eval(input("請輸入奶茶數量:"))
    total += green_tea * num_3 
    print("總金額為",total,"元")
    
    #--------9*9乘法表--------# 
  elif choose == 5 :
    for a in range(9):
      for b in range(9):
        print(a+1,"x",b+1,"=",(a+1)*(b+1))
       
    #修改含範圍--------終極密碼--------#    
  elif choose == 6 :
    code = random.randint(1,100)
    cell = 100  #設定初始上限
    floor = 1 #設定初始下限
    #print(code)

    while True:
      print("---------------------")
      print("請輸入密碼:(密碼介於{:d}~{:d}之間)".format(floor,cell))
      ans = eval(input())
      if ans == code :
        print("恭喜答對了!")
        break
      elif ans >= code and ans <= 100:
        print("密碼介於{:d}~{:d}".format(floor,ans))
        cell = ans  #設定答案為範圍上限
        continue
      elif ans <= code and ans >= 1:
        print("密碼介於{:d}~{:d}".format(ans,cell))
        floor = ans #設定答案為範圍下限
        continue
      else:
        print(input("輸入錯誤，請按任意鍵重新作答。"))
        
    #自製1--------PY升職記--------#
  elif choose == 7 :
    print("=============歡迎來到PY升職記=============\n")
    print("你好，你是一位公司業務，需要透過提升與老闆的好感度，晉升主管的位置。\n以下將有3個問題，每個問題都有對應分數，並請試著達到高分。\n")
    Q = input("(請輸入隨意鍵...開始作答)\n")

    score = 0 #初始分數

    #Question_1
    print("============第一題=============\n")
    print("早晨，你剛進公司電梯就看到老闆，請問應該如何處置呢?(A~C)")
    print("A.見面尷尬，微笑以待。\nB.精神飽滿，噓寒問暖。\nC.繼續低頭滑手機。")
    while True:
      Q1 = input("請作答:")
      optionA1 = 1
      optionB1 = 2
      optionC1 = 0
      if Q1 == "A":
        score += optionA1
        print("此題得分為{:d}分，目前分數為{:d}分\n".format(optionA1,score))
        break
      elif Q1 == "B":
        score += optionB1
        print("此題得分為{:d}分，目前分數為{:d}分\n".format(optionB1,score))
        break
      elif Q1 == "C":
        score += optionC1
        print("此題得分為{:d}分，目前分數為{:d}分\n".format(optionC1,score))
        break
      else:
        print("回復錯誤，請重新作答。\n")  
        continue
    Q = input("(請輸入隨意鍵...進入第2題)\n")

    #Question_2
    print("============第二題=============\n")
    print("工作中，老闆請你幫他買一杯咖啡，請問該如何處置呢?(A~C)")
    print("A.不要找我，我很忙。\nB.好的老闆，要喝甚麼口味的?。\nC.老闆，我可以也點一杯嗎?。")
    while True:
      Q2 = input("請作答:")
      optionA2 = 0
      optionB2 = 2
      optionC2 = 1
      if Q2 == "A":
        score += optionA2
        print("此題得分為{:d}分，目前分數為{:d}分\n".format(optionA2,score))
        break
      elif Q2 == "B":
        score += optionB2
        print("此題得分為{:d}分，目前分數為{:d}分\n".format(optionB2,score))
        break
      elif Q2 == "C":
        score += optionC2
        print("此題得分為{:d}分，目前分數為{:d}分\n".format(optionC2,score))
        break
      else:
        print("回復錯誤，請重新作答。\n")  
        continue
    Q = input("(請輸入隨意鍵...進入第3題)\n")

    #Question_3
    print("============第三題=============")
    print("下班時間到了，老闆問你今天可不可以加班，請問該如何處置?(A~C)")
    print("A.老闆，可是我晚一點還有事。\nB.好的老闆，衝衝衝!\nC.老闆，現在是下班時間，我絕不加班!")
    while True:
      Q3 = input("請作答:")
      optionA3 = 1
      optionB3 = 2
      optionC3 = 0
      if Q3 == "A":
        score += optionA3
        print("此題得分為{:d}分，目前分數為{:d}分\n".format(optionA3,score))
        break
      elif Q3 == "B":
        score += optionB3
        print("此題得分為{:d}分，目前分數為{:d}分\n".format(optionB3,score))
        break
      elif Q3 == "C":
        score += optionC3
        print("此題得分為{:d}分，目前分數為{:d}分\n".format(optionC3,score))
        break
      else:
        print("回復錯誤，請重新作答。\n")  
        continue
    Q = input("(請輸入隨意鍵，送出試卷)\n")

    print("============成績單=============\n")

    print("本試卷總分6分，你得分為{:d}分".format(score))
    if score == 6:
      print("恭喜你，獲取老闆的歡心! 晉升主管指日可待!!!\n")
    elif score < 6 and score >= 3:
      print("再努力一點，奉獻你的肝、拍你老闆馬屁，遲早升主管!!\n")
    else :
      print("只能說，有骨氣，是個狠人!!\n")
    print("-----------------------------")

    #自製2--------數字AB遊戲--------#
  elif choose == 8 :
    ans = list(random.sample(range(1,10),4)) #取 4位變數1~10
    print(ans)
    a = b = n = 0 #給初始數 a表A符合數 b表B符合數 n表取陣列n數 皆從0開始 做for迴圈。
    while a != 4:
      a = b = n = 0  #每次迴圈都回到初始0
      user = list(input("輸入四個數字："))  # 讓使用者輸入數字，並透過 list 轉換成串列
      for i in user:                     # 使用 for 迴圈，將使用者輸入的數字一一取出
        if int(user[n]) == ans[n]:    # 因為使用者輸入的是「字串」，透過 int 轉換成數字，和答案串列互相比較
          a += 1                         # 如果位置和內容都相同，就將 a 增加 1
        else:
          if int(i) in ans:           # 如果位置不同，但答案裡有包含使用者輸入的數字
            b += 1                       # 就將 b 增加 1
        n += 1                           # 因為輸入的每個數字都要判斷，將 n 增加 1
      answer = ",".join(user).replace(",","")    # 四個數字都判斷後，使用 join 將串列合併成字串
      print(answer,":{:d}A{:d}B".format(a,b))
    print("答對了!")
  

    #自製3--------21點--------可優化#
  elif choose == 9 :

    #card = random.randint(1,13)
    #print(card)
    print("----Welcome To PY_21點----")
    print("提示:本遊戲不適用「1點(A) = 11點規則」")
    random_key = input("(輸入隨意鍵開始遊戲...)")

    #-------------------------------------
    #原始點數
    bank_card = [random.randint(1,13),random.randint(1,13)] #list清單 表預設牌
    player_card = [random.randint(1,13),random.randint(1,13)]

    #玩家牌組-規則制定(11~13=10)
    if 11 in player_card:
      player_card[(player_card.index(11))] = 10
    elif 12 in player_card:
      player_card[(player_card.index(12))] = 10
    elif 13 in player_card:
      player_card[(player_card.index(13))] = 10

    #莊家牌組-規則制定(11~13=10)
    if 11 in bank_card:
      bank_card[(bank_card.index(11))] = 10
    elif 12 in bank_card:
      bank_card[(bank_card.index(12))] = 10
    elif 13 in bank_card:
      bank_card[(bank_card.index(13))] = 10

    bank_point = sum(bank_card) #莊家點數list總和
    player_point = sum(player_card) #玩家點數list總和

    print("---------------------------------")
    print("莊家的牌為{:d}+X點".format(bank_card[0]))
    print("玩家的牌為{:d}({:d}+{:d})點".format(player_point,player_card[0],player_card[1]))


    while player_point < 22:  #判斷玩家是否爆掉，沒爆進行迴圈。
      draw = input("請問是否補牌?(Y/N)")  #玩家補牌環節
      
      #玩家補牌
      if draw == "Y":
        draw_point_player = random.randint(1,13)  #賦予補牌
        
        print("(-------玩家補牌-------)")
        random_key = input("(請輸入任意鍵揭曉補牌結果...)")  #節點控制
        
        if draw_point_player >= 11: #判斷/整理"玩家"補牌點數依規則進行 11/12/13 = 10
          draw_point_player = 10
        player_point += draw_point_player #加總 sum(list)的點數跟補牌點數
        print("玩家補牌為{:d}點，目前共{:d}點".format(draw_point_player,player_point))
        if player_point > 21: #判斷玩家點數
          print("----------")
          print("莊家為{:d}點，玩家為{:d}點，爆掉了!!".format(bank_point,player_point))
          
      #玩家不補牌
      elif draw == "N":
        print("莊家的牌為{:d}({:d}+{:d})點".format(bank_point,bank_card[0],bank_card[1]))
        while bank_point < 17:
          draw_point_banker = random.randint(1,13)
          
          print("(-------莊家補牌-------)")
          Wrandom_key = input("(請輸入任意鍵揭曉補牌結果...)")  #節點控制
          
          if draw_point_banker >= 11: #判斷/整理"莊家"補牌點數依規則進行 11/12/13 = 10
            draw_point_banker = 10
          bank_point += draw_point_banker
          print("莊家補牌為{:d}點，目前共{:d}點".format(draw_point_banker,bank_point))
          if bank_point > 21: #判斷莊家點數
            print("----------")
            print("莊家為{:d}點，玩家為{:d}點，玩家贏!!".format(bank_point,player_point))
        break
    else:
      None
      
    #補充剩下情況
    if bank_point > player_point and bank_point <= 21:
      print("----------")
      print("莊家{:d}點，玩家{:d}點，莊家贏!!".format(bank_point,player_point))
    elif bank_point == player_point:
      print("----------")
      print("莊家{:d}點，玩家{:d}點，和局!!".format(bank_point,player_point))
    elif bank_point < player_point and player_point <= 21:
      print("----------")
      print("莊家{:d}點，玩家{:d}點，玩家贏!!".format(bank_point,player_point))

  elif choose == "" :
    print("輸入錯誤，系統回覆為空值!")
    
    
  else:
    print("輸入錯誤")
    
  print("-----------------------------")
  random_key = input("請輸入任意鍵回到程式主頁...")