# 정수 배열 numbers
# 문자열 길이 통일
def solution(numbers):
    # 최대 문자열 길이 탐색
    max_len = 0
    for n in numbers:
        max_len = max(max_len, len(str(n)))
    # 문자열 길이 통일
    num_list = []
    step = 0
    for n in numbers:
        if len(str(n)) < max_len:
            step = max_len - len(str(n))
            num_list.append((step * "0") + str(n))
        else:
            num_list.append(str(n))
    answer = num_list
    return answer

numbers = list(map(int, input().split()))
print(solution(numbers))