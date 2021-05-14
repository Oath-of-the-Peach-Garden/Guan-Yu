# 신규 아이디 추천
# https://programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    answer = new_id
    answer=answer.lower()
    answer=re.sub('[^-_.\w]', '', answer)
    answer=re.sub('[.]+', '.', answer)
    if len(answer)>0 and answer[0]==".":
        answer=answer[1:]
    if len(answer)>0 and answer[-1]==".":
        answer=answer[:-1]
    if len(answer)<1:
        answer="a"
    if len(answer)>15:
        answer=answer[:15]
    if answer[-1]==".":
        answer=answer[:-1]
    if len(answer)<3:
        answer+=answer[-1]*(3-len(answer))
    return answer

new_id="...!@BaT#*..y.abcdefghijklm."
new_id="z-+.^."
new_id="=.="
new_id="-_.~!@#$%^&*()=+[{]}:?,<>/._-" #"-_._-"
print(solution(new_id))