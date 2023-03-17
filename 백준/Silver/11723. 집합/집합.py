# 집합

import sys

dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0,
       11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0}

for _ in range(int(input())):
    cmd = sys.stdin.readline().rstrip().split()
    if len(cmd) == 2:
        x = int(cmd[1])

    if cmd[0] == 'add' and dic[x] == 0:
        dic[x] = 1
    elif cmd[0] == 'remove' and dic[x] == 1:
        dic[x] = 0
    elif cmd[0] == 'check':
        print(dic[x])
    elif cmd[0] == 'toggle':
        dic[x] = (dic[x]+1) % 2
    elif cmd[0] == 'all':
        dic = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1,
               11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1}
    else:
        dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0,
               11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0}
