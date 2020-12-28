while True:
    try:
        s = input()
        length = len(s)
        if length < 9:
            print('NG')
            continue
        count = 0
        if s.isupper():
            count += 1
        elif s.islower():
            count += 1
        elif s.isdigit():
            count += 1
        else:
            count += 1
        if count < 3:
            print('NG')
            continue
        for i in range(length - 3):
            if s.count(s[i:i + 3]) > 1:
                print('NG')
                break
        else:
            print('OK')
    except:
        break

map_dict = {
    'a': '2',
    'b': '2',
    'c': '2',
    'd': '3',
    'e': '3',
    'f': '3',
    'g': '4',
    'h': '4',
    'i': '4',
    'j': '5',
    'k': '5',
    'l': '5',
    'm': '6',
    'n': '6',
    'o': '6',
    'p': '7',
    'q': '7',
    'r': '7',
    's': '7',
    't': '8',
    'u': '8',
    'v': '8',
    'w': '9',
    'x': '9',
    'y': '9',
    'z': '9',
}
