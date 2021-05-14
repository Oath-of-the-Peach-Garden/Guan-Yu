# 스티커 모으기
# https://programmers.co.kr/learn/courses/30/lessons/12971

def solution(sticker):
    answer = 0
    if len(sticker)<2:
        return sticker[0]
    dp1=[0]*len(sticker)
    dp1[0]=sticker[0]
    dp1[1]=sticker[0]
    for i in range(2, len(sticker)-1):
        dp1[i]=max(dp1[i-2]+sticker[i], dp1[i-1])

    dp2=[0]*len(sticker)
    dp2[1]=sticker[1]
    for i in range(2, len(sticker)):
        dp2[i]=max(dp2[i-2]+sticker[i], dp2[i-1])

    answer=max(dp1[-2], dp2[-1])
    return answer

sticker=[14, 6, 5, 11, 3, 9, 2, 10]
print(solution(sticker))