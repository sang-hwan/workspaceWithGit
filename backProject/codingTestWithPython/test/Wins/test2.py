# 문자열 s
# 연속 문자열 갯수
def solution(s):
    # 문자열 재조합
    s_tmp = ""
    split_index = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            continue
        else:
            split_index = i
            break
    s_tmp += s[split_index+1:]
    s_tmp += s[0:split_index+1]
    print(s_tmp)
    # 연속 문자열 갯수 탐색
    count = 1
    count_list = []
    for i in range(len(s_tmp)-1):
        if s_tmp[i] == s_tmp[i+1]:
            count += 1
        else:
            count_list.append(count)
            count = 1
    count_list.append(count)
    # 연속 문자열 갯수 오름차순 정렬
    count_list.sort()
    answer = count_list
    return answer

s = input()
print(solution(s))