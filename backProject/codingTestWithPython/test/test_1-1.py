# 가능한 하위 배열을 모두 탐색
# 하위 배열들의 합을 비교
# 최대값이 갱신될 때 마다 해당 하위 배열의 시작, 끝 index를 저장

def max_array(array):
    
    start_index = 0
    end_index = 0
    max_value = 0
    
    for i in range(len(array)):
        sum = 0
        for j in range(i, len(array)):
            sum += array[j]
            if sum >= max_value:
                max_value = sum
                start_index = i
                end_index = j
    
    return max_value, start_index, end_index

array = list(map(int, input().split()))
max_value, start_index, end_index = max_array(array)
print(array[start_index:end_index+1], end = '')
print(", ", end="")
print(max_value)