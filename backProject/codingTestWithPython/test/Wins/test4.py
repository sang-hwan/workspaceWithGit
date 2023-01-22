# [방호수]이름1, 이름2, ... 형식의 rooms
# 자리가 생긴 방번호 target
# target에 배정될 수 있는 직원 우선 순위
def solution(rooms, target):
    # {방번호 : 직원} dict 생성
    r_p_dict = {}
    split_i = 0
    for r in rooms:
        for i, e in enumerate(r):
            if e == "]":
                split_i = i
            else:
                continue
        r_p_dict[int(r[1:split_i])] = r[split_i+1:].split(",")
    # 새 방번호랑 같은 방번호 제외
    for k, v in list(r_p_dict.items()):
        if k == target:
            del r_p_dict[k]
        else:
            continue
    # {직원 : 배정된 방 갯수} dict 생성
    p_c_dict = {}
    p_list = list(r_p_dict.values())
    p_set = []
    for peoples in p_list:
        for p in peoples:
            if p not in p_set:
                p_set.append(p)
            else:
                continue
    count = 0
    for p in p_set:
        for peoples in p_list:
            for c in peoples:
                if p == c:
                    count += 1
                else:
                    continue
        p_c_dict[p] = count
        count = 0
    # 1. 배정된 방 갯수 2. 새 방번호와 가까운 방번호
    sorted_p_c_dict = sorted(p_c_dict.items(), key=lambda item:(item[1], item[0]))
    # print(f"sorted_p_c_dict:{sorted_p_c_dict}")
    diff_r_p_dict = {}
    for k, v in r_p_dict.items():
        diff_r_p_dict[abs(k-target)] = v
    sorted_r_p_dict = sorted(diff_r_p_dict.items(), key=lambda item:item[0])
    # print(f"sorted_r_p_dict:{sorted_r_p_dict}")
    answer_dict = {}
    answer_dict_list = []
    for p in sorted_p_c_dict:
        for e in sorted_r_p_dict:
            if p[0] in e[1]:
                answer_dict["people"] = p[0]
                answer_dict["count"] = p[1]
                answer_dict["abs_r"] = e[0]
                answer_dict_list.append(answer_dict.copy())
                # print(f"answer_dict:{answer_dict}")
                # print(f"answer_dict_list:{answer_dict_list}")
                break
            else:
                continue
    sorted_answer_dict_list = sorted(answer_dict_list, key=lambda item:(item["count"], item["abs_r"], item["people"]))
    print(f"sorted_answer_dict_list:{sorted_answer_dict_list}")
    answer = []
    for p in sorted_answer_dict_list:
        answer.append(p["people"])
                    
    return answer

rooms = input().split()
target = int(input())
print(solution(rooms, target))