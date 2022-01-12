text = input("Введите строку: ")
upper = 0
lower = 0

for element in text:
    if element.isupper():
        upper += 1
    elif element.islower():
        lower += 1

if upper > lower:
    text = text.upper()
else:
    text = text.lower()

print(text)
