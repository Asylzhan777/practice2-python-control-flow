# Пример 3: while с continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

nums = [3, -2, 6, -1, 9]
i = 0

while i < len(nums):
    if nums[i] < 0:
        i += 1
        continue
    print(nums[i])
    i += 1

words = ["hi", "ok", "python", "a", "code"]
i = 0

while i < len(words):
    if len(words[i]) < 3:
        i += 1
        continue
    print(words[i])
    i += 1
