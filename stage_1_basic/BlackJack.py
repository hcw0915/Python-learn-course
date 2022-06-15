import random

#card = random.randint(1,13)
#print(card)
print("----Welcome To PY_BlackJack----")
key = input("(輸入隨意鍵開始遊戲...)")

#-------------------------------------
bank_card = [random.randint(1,13),random.randint(1,13)]
player_card = [random.randint(1,13),random.randint(1,13)]

#print(player_card) #原始點數
#print(bank_card)

#玩家牌組
if 11 in player_card:
  player_card[(player_card.index(11))] = 10
elif 12 in player_card:
  player_card[(player_card.index(12))] = 10
elif 13 in player_card:
  player_card[(player_card.index(13))] = 10

#莊家牌組
if 11 in bank_card:
  bank_card[(bank_card.index(11))] = 10
elif 12 in bank_card:
  bank_card[(bank_card.index(12))] = 10
elif 13 in bank_card:
  bank_card[(bank_card.index(13))] = 10

#print(player_card) #修正後點數
#print(bank_card)

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
    Q = input("(請輸入任意鍵揭曉補牌結果...)")  #節點控制
    
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
      W = input("(請輸入任意鍵揭曉補牌結果...)")  #節點控制
      
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


