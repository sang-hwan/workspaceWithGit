# 각 종류의 열림 괄호에 서로 다른 숫자를 부여
# {: 1, (: 2, [: 3
# 열림 괄호와 종류가 같은 닫힘 괄호에 음의 부호를 붙인 같은 숫자를 부여
# }: -1, ): -2, ]: -3
# 해당 숫자들로 입력 값의 총 합을 계산하여 0이면 True, 아니면 False를 리턴

def valid(array):
    
    summary = 0
    
    for i in array:
        if i == '{':
            num = 1
        elif i == '(':
            num = 2
        elif i == '[':
            num = 3
        elif i == '}':
            num = -1
        elif i == ')':
            num = -2
        elif i == ']':
            num = -3
        else:
            return "규정에 맞지 않는 입력 데이터입니다"
        summary += num
        
    if summary == 0:
        return "True"
    else:
        return "False"

array = list(input())
print(valid(array))