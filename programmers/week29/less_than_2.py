# 2개 이하로 다른 비트
# https://programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    answer = []
    for num in numbers:
        num_bin=bin(num)[2:]
        print(num_bin)
        i=1
        while True:
            tmp_num=bin(num+i)[2:]
            num_bin='0'*(len(tmp_num)-len(num_bin))+num_bin
            cnt=0
            print(f'{num_bin} {tmp_num}')
            for a,b in zip(num_bin, tmp_num):
                if a!=b:
                    cnt+=1
                if cnt>2:
                    break
            else:
                answer.append(num+i)
                break
            i+=1
    return answer

print(solution([2,7]))