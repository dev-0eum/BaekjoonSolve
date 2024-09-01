import sys

line = sys.stdin.readline()
answer = ''
stack = []

for x in line:
    # Alphabet
    if x.isalpha():
        answer += x
    # expression
    else:
        if x == '(':
            stack.append(x)

        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            stack.append(x)

        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(x)

        elif x == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop() # ?
#     print('answer: ',answer)
#     print("token: ",x)
#     print(stack)
#     print()

while stack:
    answer += stack.pop()
print(answer)