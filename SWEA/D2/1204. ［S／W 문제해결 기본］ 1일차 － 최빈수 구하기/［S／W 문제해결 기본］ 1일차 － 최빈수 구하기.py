# 최빈수 구하기

T = int(input())

for i in range(T):
    max = 0
    mode = 0
    index = int(input())
    scr = list(map(int,input().split()))    
    scr.sort()
    set_lst = list(set(scr))

    for j in range(len(set_lst)):
        tmp = scr.count(set_lst[j])
        if max <= tmp:
            max = tmp
            mode = set_lst[j]
    print(f'#{index} {mode}')