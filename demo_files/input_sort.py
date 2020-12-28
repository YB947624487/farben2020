# while True:
#     try:
#         s = input().strip()
#         l = []
#         other_l = []
#         count = 0
#         for i in s:
#             if i.isalpha():
#                 l.append((i, ord(i.lower())))
#             else:
#                 other_l.append((i, count))
#             count += 1
#         sort_l = sorted(l, key=lambda x: x[1])
#         for i in other_l:
#             sort_l.insert(i[1], i)
#         res_list = [i[0] for i in sort_l]
#         print("".join(res_list))
#     except:
#         break


# from collections import Counter
#
#
# def is_brother_word(k, s):
#     if k == s or len(k) != len(s):
#         return False
#     k_counter = Counter(k)
#     s_counter = Counter(s)
#     if k_counter == s_counter:
#         return True
#     return False
#
#
# while True:
#     try:
#         s_list = input().strip().split()
#         n = int(s_list[0])
#         w_list = s_list[1:n + 1]
#         key = s_list[-2]
#         res_list_index = int(s_list[-1])
#         res_list = []
#         for i in w_list:
#             if is_brother_word(key, i):
#                 res_list.append(i)
#         n_res_list = len(res_list)
#         print(n_res_list)
#         res_list.sort()
#         if res_list_index -1 < n_res_list:
#             print(res_list[res_list_index-1])
#     except:
#         break

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

def encode_pwd(s):
    res = ""
    for i in s:
        if i.isupper():
            if i == "Z":
                res += "a"
                continue
            res += chr(ord(i) + 1).lower()
        elif i.islower():
            if i == "z":
                res += "A"
                continue
            res += chr(ord(i) + 1).upper()
        elif i.isdigit():
            if i == "9":
                res += "0"
                continue
            res += chr(ord(i) + 1)
        else:
            break
    return res


def decode_pwd(s):
    res = ""
    for i in s:
        if i.isupper():
            if i == "A":
                res += "z"
                continue
            res += chr(ord(i) - 1).lower()
        elif i.islower():
            if i == "a":
                res += "Z"
                continue
            res += chr(ord(i) - 1).upper()
        elif i.isdigit():
            if i == "0":
                res += "9"
                continue
            res += chr(ord(i) - 1)
        else:
            break
    return res


while True:
    try:
        encode_s = input().strip()
        decode_s = input().strip()
        print(encode_pwd(encode_s))
        print(decode_pwd(decode_s))
    except:
        break
