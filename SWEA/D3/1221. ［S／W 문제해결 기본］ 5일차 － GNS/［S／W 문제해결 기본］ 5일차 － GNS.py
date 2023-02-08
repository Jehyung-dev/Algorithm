# [S/W 문제해결 기본] 5일차 - GNS

for _ in range(int(input())):
    idx, length = input().split()
    arr = list(input().split())
    dic = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0,
           'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0, }
    for i in arr:
        dic[i] += 1
    print(idx)
    for j in dic.keys():
        for _ in range(dic[j]):
            print(j, end=' ')
