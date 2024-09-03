import sys

while True:
    line = sys.stdin.readline()
    if line == "":
        break
     
    small = 0
    big = 0
    num = 0
    blank = 0

    for x in line:
        if x.isalpha():
            if ord(x) >= 97 and ord(x) <= 122:
                small += 1
            elif ord(x) >=65 and ord(x) <=90:
                big += 1
        elif x.isnumeric():
            num += 1
        elif x == " ":
            blank += 1
    
    print(small,big,num,blank)
