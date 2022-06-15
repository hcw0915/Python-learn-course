from sys import exit


print("歡迎來到PY升職記")
name = input("請輸入你的名字:")
#print("請輸入你的性別(1/2):\n1.男性\n2.女性")
#gender = input()

print("==========================")
print(name,"你好，你是一位公司業務，需要透過提升與老闆的好感度，晉升主管的位置。\n以下將有3個問題，每個問題都有對應分數，並請試著達到高分。")
Q = input("(請輸入隨意鍵...開始作答)\n")

score = 0

#Question_1
print("============第一題=============")
print("早晨，你剛進公司電梯就看到老闆，請問應該如何處置呢?(A~C)")
print("A.見面尷尬，微笑以待。\nB.精神飽滿，噓寒問暖。\nC.繼續低頭滑手機。")
Q1 = input("請作答:")
optionA1 = 1
optionB1 = 2
optionC1 = 0
if Q1 == "A":
  score += optionA1
  print("此題得分為{:d}分，目前分數為{:d}分".format(optionA1,score))
elif Q1 == "B":
  score += optionB1
  print("此題得分為{:d}分，目前分數為{:d}分".format(optionB1,score))
elif Q1 == "C":
  score += optionC1
  print("此題得分為{:d}分，目前分數為{:d}分".format(optionC1,score))
else:
  print("回復錯誤，請重新作答。")  #這裡要塞迴圈loop!!!


Q = input("(請輸入隨意鍵...進入第2題)\n")


#Question_2
print("============第二題=============")
print("工作中，老闆請你幫他買一杯咖啡，請問該如何處置呢?(A~C)")
print("A.不要找我，我很忙。\nB.好的老闆，要喝甚麼口味的?。\nC.老闆，我可以也點一杯嗎?。")
Q2 = input("請作答:")
optionA2 = 0
optionB2 = 2
optionC2 = 1
if Q2 == "A":
  score += optionA2
  print("此題得分為{:d}分，目前分數為{:d}分".format(optionA2,score))
elif Q2 == "B":
  score += optionB2
  print("此題得分為{:d}分，目前分數為{:d}分".format(optionB2,score))
elif Q2 == "C":
  score += optionC2
  print("此題得分為{:d}分，目前分數為{:d}分".format(optionC2,score))
else:
  print("回復錯誤，請重新作答。")  #這裡要塞迴圈loop!!!
  

Q = input("(請輸入隨意鍵...進入第3題)\n")

#Question_3
print("============第三題=============")
print("下班時間到了，老闆問你今天可不可以加班，請問該如何處置?(A~C)")
print("A.老闆，可是我晚一點還有事。\nB.好的老闆，衝衝衝!\nC.老闆，現在是下班時間，我絕不加班!")
Q3 = input("請作答:")
optionA3 = 1
optionB3 = 2
optionC3 = 0
if Q3 == "A":
  score += optionA3
  print("此題得分為{:d}分，目前分數為{:d}分".format(optionA3,score))
elif Q3 == "B":
  score += optionB3
  print("此題得分為{:d}分，目前分數為{:d}分".format(optionB3,score))
elif Q3 == "C":
  score += optionC3
  print("此題得分為{:d}分，目前分數為{:d}分".format(optionC3,score))
Q = input("(請輸入隨意鍵，送出試卷)\n")
print("============成績單=============\n")

print("本試卷總分6分，你得分為{:d}分".format(score))
if score == 6:
  print("恭喜你，獲取老闆的歡心! 晉升主管指日可待!!!")
elif score < 6 and score >= 3:
  print("再努力一點，奉獻你的肝、拍你老闆馬屁，遲早升主管!!")
else :
  print("只能說，有骨氣，是個狠人!!")
  exit()
