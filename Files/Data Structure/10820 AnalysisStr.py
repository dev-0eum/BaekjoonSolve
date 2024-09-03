# 소문자 대문자 숫자 공백

import sys
while True:
    line = sys.stdin.readline()
    if line == "":
        print("STOP")
        break
     
    small = 0
    big = 0
    num = 0
    blank = 0

    for x in line:
        if x.isalpha():
            if ord(x) >= 97: # 소문자
                pass
            elif True:
                pass
        elif x.isnumeric():
            num += 1
        elif x == " ":
            blank += 1
    

    print(line)
