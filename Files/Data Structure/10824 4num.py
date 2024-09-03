word = input().split()
words = ['','']

words[0] = word[0]+word[1]
words[1] = word[2]+word[3]

print(int(words[0]) + int(words[1]))