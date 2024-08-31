import sys
s = sys.stdin.readline()
sub = ""
answer = ""

def flip(line):
    words = []
    reversed = ''

    words = line.split(" ")
    
    for word in words:
        lst = list(word)
        lst.reverse()

        if("\n" in word):
            lst.remove("\n")
        reversed += ''.join(lst)
        reversed += " "
    return reversed.rstrip()

# if there is tag
if s.find("<") != -1:
    # first fliter : tag <>
    while s.find("<") != -1:
        l = s.find("<")
        r = s.find(">")
        # text
        sub = s[0:l]
        sub = flip(sub)
        if sub.strip() != "":
            answer += sub
        # tag
        sub = s[l:r+1]
        answer += sub

        s = s[r+1:]
    
    if s:
        answer += flip(s)
    print(answer)
# only text
else:
    print(flip(s))