# 멀리뛰기

def solution(n):
  dp=[1,1]+[0]*(n-1)
  for i in range(2,n+1):
    dp[i]=(dp[i-2]+dp[i-1])%1234567
  return dp[n]

print(solution(4))