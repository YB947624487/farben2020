# def left_max(arr):
#     n = len(arr)
#     res = [1]*n
#     for i in range(n):
#         for j in range(i):
#             if arr[j] < arr[i] and res[j] + 1 > res[i]:
#                 res[i] = res[j] + 1
#     return res
#
# def right_max(arr):
#     n = len(arr)
#     res = [1] * n
#     for i in range(n-1,-1,-1):
#         for j in range(i+1,n):
#             if arr[j] < arr[i] and res[j] + 1 > res[i]:
#                 res[i] = res[j] + 1
#     return res
#
# while True:
#     try:
#         s_list = list(map(int,input().strip().split()))
#         l_list = left_max(s_list)
#         r_list = right_max(s_list)
#         sum_list = []
#         n = len(l_list)
#         for i in range(n):
#             sum_list.append(l_list[i]+r_list[i]-1)
#         print(n-max(sum_list))
#     except:
#         break

def left_max(arr):
    n = len(arr)
    res = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and res[j] + 1 > res[i]:
                res[i] = res[j] + 1
    return res


def right_max(arr):
    n = len(arr)
    res = [1] * n
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if arr[j] < arr[i] and res[j] + 1 > res[i]:
                res[i] = res[j] + 1
    return res


while True:
    try:
        n = int(input().strip())
        s_list = list(map(int, input().strip().split()))
        if n != len(s_list):
            continue
        l_list = left_max(s_list)
        r_list = right_max(s_list)
        sum_list = []
        for i in range(n):
            sum_list.append(l_list[i] + r_list[i] - 1)
        print(n - max(sum_list))
    except:
        break
