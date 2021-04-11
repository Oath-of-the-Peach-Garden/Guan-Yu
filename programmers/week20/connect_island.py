# 섬 연결하기
# https://programmers.co.kr/learn/courses/30/lessons/42861
from collections import deque

def solution(n, costs):
  answer = 0
  matrix=[ [0]*n for _ in range(n)]
  for a,b,i in costs:
    matrix[a][b]=i
    matrix[b][a]=i
  print(matrix)
  cost=[]
  for i in range(n):
    queue=deque()
    queue.append(i)
    while queue:
      
  return answer

n=4
costs=[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n,costs))