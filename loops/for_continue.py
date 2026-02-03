# Пример 6: for с continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

for i in range(10):
    if i == 5:
        continue
    print(i)

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

nums = [3, -1, 5, -7, 9]

for n in nums:
    if n < 0:
        continue
    print(n)

words = ["hi", "hello", "a", "python", "ok"]

for w in words:
    if len(w) < 3:
        continue
    print(w)
