# 다솔이의 다이아몬드 장식

for t in range(int(input())):
    N = input()
    if len(N) == 1:
        s1 = '..#' + '..#' * (len(N) - 1) + '..'
    else:
        s1 = '..#' + '...#' * (len(N) - 1) + '..'
    s2 = '.#' * 2 * len(N) + '.\n'
    s3 = '#.' + '.#.'.join(N) + '.#\n'
    s = s1 + '\n' + s2 + s3 + s2 + s1
    print(s)
