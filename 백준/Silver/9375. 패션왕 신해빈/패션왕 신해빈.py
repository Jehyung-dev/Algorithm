# 패션왕 신해빈

for _ in range(int(input())):
    dic = {}
    ans = 1

    for _ in range(int(input())):
        name, cate = input().split()
        if cate in dic:
            dic[cate] += 1
        else:
            dic[cate] = 1

    for i in dic:
        ans *= dic[i]+1
    print(ans-1)
