import sys
input = sys.stdin.readline()

words = []
reversed = ''
for x in range(int(input)):
    line = sys.stdin.readline()
    words = line.split(" ")
    
    for word in words:
        lst = list(word)
        lst.reverse()

        if("\n" in word):
            lst.remove("\n")
        reversed += ''.join(lst)
        reversed += " "

    print(reversed)
    reversed = ''