# 크레인 인형뽑기 게임
from collections import deque

def solution(board, moves):
    answer = 0
    n=len(board)
    board_list=[ deque() for _ in range(n)]
    for b in board:
        for i in range(n):
            if b[i]!=0:
                board_list[i].append(b[i])
    print(board_list)
    stack=[]
    for m in moves:
        if board_list[m-1]:
            if stack and stack[-1]==board_list[m-1][0]:
                stack.pop()
                answer+=1
            else:
                stack.append(board_list[m-1].popleft())
    answer*=2
    return answer

board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]	
print(solution(board, moves))