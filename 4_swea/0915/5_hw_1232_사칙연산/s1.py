# import sys
# sys.stdin = open('input.txt', 'r')

def evaluate_tree(n):

    if not tree_path[n]:
        return tree_value[n]
    
    if tree_value[n] == '+':
        return evaluate_tree(tree_path[n][0]) + evaluate_tree(tree_path[n][1])
    if tree_value[n] == '-':
        return evaluate_tree(tree_path[n][0]) - evaluate_tree(tree_path[n][1])
    if tree_value[n] == '*':
        return evaluate_tree(tree_path[n][0]) * evaluate_tree(tree_path[n][1])
    if tree_value[n] == '/':
        return evaluate_tree(tree_path[n][0]) / evaluate_tree(tree_path[n][1])
        

for t in range(1, 11):
    N = int(input())
    tree_value = [0] * (N + 1)
    tree_path = [0] * (N + 1)
    for i in range(1, N + 1):
        info = list(input().split())
        if len(info) == 4:
            tree_path[i] = (int(info[2]), int(info[3]))
            tree_value[i] = info[1]
        else:
            tree_value[i] = int(info[1])
    
    ans = int(evaluate_tree(1))
    
    print(f'#{t}', ans)