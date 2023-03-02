# 자리배정

def Seat(r, c):
    global arr, ans_x, ans_y
    di, n = 0, 1
    while n <= r_num * c_num:
        arr[r][c] = n
        if n == point:
            ans_x, ans_y = c + 1, r_num - r
        nr, nc = r + dr[di], c + dc[di]
        if 0 <= nr < r_num and 0 <= nc < c_num and not arr[nr][nc]:
            r, c = nr, nc
            n += 1
        else:
            di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]
            n += 1


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
c_num, r_num = map(int, input().split())
point = int(input())
arr = [[0] * c_num for _ in range(r_num)]
ans_x = ans_y = 0
Seat(r_num - 1, 0)

if ans_x:
    print(ans_x, ans_y)
else:
    print(ans_x)
