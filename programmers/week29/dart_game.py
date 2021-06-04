# 다트 게임
# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    score=[]
    i=0
    temp_score=""
    while i < len(dartResult):
        if ord(dartResult[i]) in range(48,58):
            if temp_score!="":
                score.append(temp_score)
            temp_score=dartResult[i]+dartResult[i+1]
            i+=1
        else:
            temp_score+=dartResult[i]
        i+=1
    score.append(temp_score)

    bonus={"S":1,"D":2,"T":3}
    score_num=[0]
    for s in score:
        num=s[0]
        i=1
        while i<len(s):
            if ord(s[i]) in range(48,58):
                num+=s[i]
            num=int(num)
            if s[i] in bonus.keys():
                num=num**bonus[s[i]]
            if s[i] == "*":
                num=num*2
                score_num[-1]=score_num[-1]*2
            if s[i] == "#":
                num=num*(-1)
            i+=1
        score_num.append(num)

    answer = 0
    for num in score_num:
        answer+=num
    
    return answer