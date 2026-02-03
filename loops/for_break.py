# Пример 5: for с break
for i in range(1, 6):
    if i == 4:
        break
    print(i)

for i in range(10):
    if i == 5:
        break
    print(i)

numbers = [1, 3, 7, 9, 11]

for n in numbers:
    if n == 7:
        print("Нашли 7!")
        break

nums = [4, 6, 2, -1, 8]

for n in nums:
    if n < 0:
        break
    print(n)

passwords = ["1234", "qwerty", "admin", "secret"]

for p in passwords:
    if p == "admin":
        print("Доступ запрещён")
        break
