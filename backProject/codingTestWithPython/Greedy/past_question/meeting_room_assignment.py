# n 입력
n = int(input())

# 회의 시간 입력
time = []
for _ in range(n):
    begin, end = map(int, input().split())
    time.append((begin, end))
    
# 회의 시간 종료 기준 오름차순
time.sort(key=lambda x:x[1])

# 회의 종료 시간과 다음 회의 시작 시간을 비교
# 회의 종료 시간이 다음 회의 시작 시간보다 작으면 최종 종료 시간 갱신
# 회의 가능 여부 +1
answer = 0
last_end = 0
for begin, end in time:
    if last_end<=begin:
        answer += 1
        last_end = end

print(answer)