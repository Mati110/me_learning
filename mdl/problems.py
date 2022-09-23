# Count   
def minion_game(string):
    s = str.upper(string)
    max_len = 10**6
    p_stu, p_kev, c, b = 0, 0, 0, 0
    w_stu, w_kev = [], []
    if 0 < len(s) <= max_len:
        for i in s:
            if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
                b = len(s)
                for r in range(len(s[c:])):
                    w_kev.append(s[c:b])
                    b -= 1
                    p_kev += 1
            else:
                b = len(s)
                for r in range(len(s[c:])):
                    w_stu.append(s[c:b])
                    b -= 1
                    p_stu += 1
            c += 1
    if p_stu > p_kev:
        res = f"Stuart %s" % p_stu
    elif p_stu < p_kev:
        res = f"Kevin %s" % p_kev
    else:
        res = "Draw"
    print(res)
    print(p_stu, w_stu)
    print(p_kev, w_kev)


def minion_game_r(string):
    length = len(string)
    vowels = 'AEIOU'
    vowel_score = 0
    consonant_score = 0
    for i, char in enumerate(string):
        if vowels.count(char) == 1:
            print(length)
            vowel_score += length - i
        else:
            print(length)
            consonant_score += length - i
    if vowel_score == consonant_score:
        print("Draw")
    elif vowel_score > consonant_score:
        print("Kevin", vowel_score)
    else:
        print("Stuart", consonant_score)


def plus_minus(arr):
    np = 0
    nn = 0
    nc = 0
    for i in arr:
        if i > 0:
            np += 1
        elif i < 0:
            nn += 1
        else:
            nc += 1
    print("{:6f}".format(np / len(arr)))
    print("{:6f}".format(nn / len(arr)))
    print("{:6f}".format(nc / len(arr)))


def mini_max_sum(arr):
    res = 0
    larr = len(arr)
    for i in range(larr):
        res += arr[i]
    arr = sorted(arr)
    print(res - arr[4], end=" ")
    print(res - arr[0])


def time_conversion(s):
    res = s[0:-2]
    if s[-2:] == "PM":
        if int(s[0:2]) != 12:
            h = int(s[0:2]) + 12
        else:
            h = "12"
        res = str(h) + s[2:-2]
    elif int(s[0:2]) == 12:
        h = "00"
        res = str(h) + s[2:-2]
    return res


def time_conversion_r(s):
    h = int(s[:2])
    is_am = s[-2:] == 'AM'

    result_hour = h % 12 if is_am else (h % 12) + 12
    print(h % 12)
    return f"{result_hour:02}{s[2:-2]}"


def lonely_integer(a):
    a = sorted(a)
    u = 0
    if 1 <= len(a) < 100 and len(a) % 2 != 0:
        if len(a) == 1:
            u = a[0]
        else:
            for i in range(len(a)):
                if a[i-2] != a[i-1] and a[i-1] != a[i]:
                    return a[i-1]
    return u


def fizz_buzz(n):
    if 0 < n < 2 * (10 ** 5):
        for i in range(n):
            if (int(i)+1) % 3 != 0 and (int(i)+1) % 5 != 0:
                print(str(i+1))
            else:
                fb = ""
                if (int(i)+1) % 3 == 0:
                    fb = "Fizz"
                if (int(i)+1) % 5 == 0:
                    fb = fb + "Buzz"
                print(fb)


def create_random(big):
    x = memoryview(bytes(5))
    c = 0
    for i in str(x):
        try:
            if int(i) % 2 == 0:
                c += int(i)
            else:
                c -= int(i)
        except ValueError:
            c += int(c / 1.2)
    if c < 0:
        c *= -1
    while c > big:
        c -= c / 10
    return int(c)


def diagonal_difference(arr):
    ab = 0
    for i in range(len(arr)):
        ab = ab + arr[i][i] - arr[i][(i+1)*-1]
    return ab if ab >= 0 else ab * -1
