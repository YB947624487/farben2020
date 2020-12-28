def func(s):
    hex_num = int(s, 16)
    bin_str = bin(hex_num)
    reverse_bin_num = "0b" + "".join(list(bin_str)[2:][::-1])
    hex_str = hex(int(reverse_bin_num, 2))[2:].upper()
    return hex_str


while True:
    try:
        s1 = input().strip()
        s2 = input().strip()
        s_list = list(s1 + s2)
        s_list[0::2] = sorted(s_list[0::2])
        s_list[1::2] = sorted(s_list[1::2])
        res = ""
        for i in s_list:
            if i.isdigit() or i.lower() in "abcdef":
                res += func(i)
            else:
                res += i
        print(res)

    except:
        break
