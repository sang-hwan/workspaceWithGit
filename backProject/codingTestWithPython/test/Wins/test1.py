# 자연수 배열 numbers
# 과반수 차지하는 숫자
# 없으면 -1
def solution(numbers):
    answer = 0
    # numbers의 원소별 갯수 탐색
    count_list = [0] * 100
    for n in numbers:
        count_list[n] += 1
    # numbers의 원소별 갯수 중 최댓값
    count_max = 0
    max_index = 0
    for i, e in enumerate(count_list):
        if e == 0:
            continue
        else:
            if count_max < e:
                max_index = i
                count_max = e
            else:
                continue
    # 과반수 차지하는 숫자인지 확인
    if len(numbers)//2 < count_list[max_index]:
        answer = max_index
    else:
        answer = -1
    
    return answer
    
numbers = list(map(int, input().split())) # 배열 입력
print(solution(numbers))