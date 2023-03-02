# 크로아티아 알파벳

alpha = {'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='}
s = input()
i = cnt = 0
ans = ''

while i < len(s):
    if i + 2 < len(s):
        if s[i:i + 3] in alpha:
            cnt += 1
            i += 3
            continue
    if i + 1 < len(s):
        if s[i:i + 2] in alpha:
            cnt += 1
            i += 2
            continue
    cnt += 1
    i += 1
    
print(cnt)
