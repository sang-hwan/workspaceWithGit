# mine answer
# n = input()
# length = len(n)
# max = 0

# for i in range(length):
#     if int(n[i]) > 1:
#         if max != 0:
#             max *= int(n[i])
#         else:
#             max = 1
#             max *= int(n[i])
#     elif int(n[i]) == 1:
#        max += 1
#     else:
#         continue

# print(max)

# book answer
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])
for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num<=1 or result<=1:
        result += num
    else:
        result *= num
        
print(result)