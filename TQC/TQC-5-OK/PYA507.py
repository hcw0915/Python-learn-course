def compute(n): 
  if n <= 0:  #判斷是否小於0
    return "Not Prime"  
  for i in range(2,n):  #界定i 的範圍會再2~n之間  2,3,4,5,6....,n-1  
    if n % i == 0:  # 如果 n/i(在i不等於n的情況下)的餘數=0(表示整除)，就表示 n 有 非n的數 可以被整除 就不是質數。
      return "Not Prime"
    else:
      return "Prime"  
# 用return 只會回傳1個答案， 如果用print 會依照i=2,3,4,5,6.....n-1每次結果做回傳。
n=eval(input())
print(compute(n))

"""
Prime
Not Prime
"""