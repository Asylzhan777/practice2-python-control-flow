# Пример 2: while с break
i = 1
while True:
    print(i)
    if i == 3:
        break
    i += 1

i = 0
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1

nums = [2, 4, 6, 8, 10]
i = 0

while i < len(nums):
    if nums[i] == 6:
        print("Нашли 6!")
        break
    i += 1

while True:
    password = input("Введите пароль: ")
    if password == "1234":
        print("Доступ разрешён")
        break

nums = [5, 7, 3, -2, 9]
i = 0

while i < len(nums):
    if nums[i] < 0:
        break
    print(nums[i])
    i += 1

