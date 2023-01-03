n, k = map(int, input().split()) # n과 k를 입력받기
a = list(map(int, input().split())) # 배열 a의 모든 원소를 입력받기
b = list(map(int, input().split())) # 배열 b의 모든 원소를 입력받기

a.sort() # 배열 a는 오름차순 정렬 수행
b.sort(reverse=True) # 배열 b는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k번 비교
for i in range(k):
    # a의 원소가 b의 원소보다 작은 경우
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else: # a의 원소가 b의 원소보다 크거나 같을 때, 반복문을 탈출
        break
    
print(sum(a)) # 배열 a의 모든 원소의 합을 출력