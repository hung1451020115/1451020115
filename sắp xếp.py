list = [3,54,6,7,8,9]
k = len(list)

for i in range(0, k - 1):
    for j in range(i + 1, k):
        if (list[i] > list[j]):
            tmp = list[i]
            list[i] = list[j]
            list[j] = tmp

print(list)