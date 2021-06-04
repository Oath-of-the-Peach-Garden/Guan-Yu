# 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681


def solution(n, arr1, arr2):
    temp_arr=[]
    for i in range(n):
        temp_arr.append([" "]*n)
    for i,a1,a2 in zip(range(n),arr1,arr2):
        temp1=a1
        temp2=a2
        for j in range(n-1,-1,-1):
            if temp1%2==1 or temp2%2==1:
                temp_arr[i][j]="#"
            temp1//=2
            temp2//=2
    answer=[""]*n
    for i in range(n):
        answer[i]="".join(temp_arr[i])
    return answer

n=5
arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))