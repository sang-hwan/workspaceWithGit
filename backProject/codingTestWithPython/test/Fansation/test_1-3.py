def valid(array):
    
    stack = []
    
    for a in array:
        if a == '{' or a=='(' or a=='[':
            stack.append(a)
        else:
            if len(stack) == 0:
                return 0
            else:
                pop_a = stack.pop()
                if pop_a == '{' and a == '}':
                    continue
                elif pop_a == '(' and a == ')':
                    continue
                elif pop_a == '[' and a == ']':
                    continue
                else:
                    return 0
    return 1
            
array = list(input())
if valid(array) == 1:
    print(True)
else:
    print(False)