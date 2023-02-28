# [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드

code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
        '0110111': 8, '0001011': 9}
T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    end_r = end_c = odd = even = 0
    pwd, s = [], ''

    for i in range(N):
        for j in range(M):
            if arr[i][j] == '1':
                end_r, end_c = i, j
        if end_c:
            break
    temp = arr[end_r]
    temp = temp[end_c - 55:end_c + 1]

    for k in temp:
        s += k
        if len(s) == 7:
            pwd.append(code[s])
            s = ''

    for i in range(1, 9):
        if i % 2:
            odd += pwd[i - 1]
        else:
            even += pwd[i - 1]

    if not (odd * 3 + even) % 10:
        print(f'#{t} {sum(pwd)}')
    else:
        print(f'#{t} 0')
