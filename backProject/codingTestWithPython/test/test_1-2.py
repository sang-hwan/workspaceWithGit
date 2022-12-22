# 이진 트리의 노드 수는 2배수로 증가
# 입력된 총 노드 수를 2배수로 빼주면 깊이를 구할 수 있을 것으로 생각

def maxDepth(root):

    if len(root) != 0:
        depth_nodes = 1
        depth = 1
        total_nodes = len(root)
        while True:
            total_nodes -= depth_nodes
            if total_nodes != 0:
                depth_nodes *= 2
                depth += 1
            else:
                return depth
    else:
        return 0
        
root = list(input().split())
print(maxDepth(root))