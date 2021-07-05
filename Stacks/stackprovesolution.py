stack = []

phrase = input("Please input a phrase: ")

for letter in phrase:
    stack.append(letter)

result = ""

while len(stack) > 0:
    result += stack.pop()

print(f"\nThe phrase you entered was: {phrase}\nThe reversed phrase is: {result}")
