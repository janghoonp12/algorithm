numbers = [
    ['###', '#.#', '#.#', '#.#', '###'],
    ['..#', '..#', '..#', '..#', '..#'],
    ['###', '..#', '###', '#..', '###'],
    ['###', '..#', '###', '..#', '###'],
    ['#.#', '#.#', '###', '..#', '..#'],
    ['###', '#..', '###', '..#', '###'],
    ['###', '#..', '###', '#.#', '###'],
    ['###', '..#', '..#', '..#', '..#'],
    ['###', '#.#', '###', '#.#', '###'],
    ['###', '#.#', '###', '..#', '###'],
]

arr = [list(input().split()) for i in range(5)]
ans = [0 for i in range(4)]
for i in range(4):
    for j in range(10):
        flag = False
        for k in range(5):
            for l in range(3):
                if arr[k][i][l] == '#' and numbers[j][k][l] == '.':
                    flag = True
                    break
            if flag:
                break
        else:
            ans[i] = j
            break
print(f'{ans[0]}{ans[1]}:{ans[2]}{ans[3]}')