# TODO

score = []  
for i in range(10):
  n = eval(input())
  score += [n]

total = sum(score)-max(score)-min(score)  # 總數 =10數總和-最大-最小
avg = total/8
print(total)
print("%.2f" %avg)

#score.remove(max(score))