p = int(input())
d = {}
l = []
for i in range(p):
    l.append(input())

for i in l:
    count = 0
    j = i + "_"
    for idx in range(l1):
        if key.startswith(j):
            count = count if int(key.split("_")[1]) < count else int(key.split('_')[1])
    count = count + 1
    key  = i + "_" + str(count)
    d[key] = count
for key in d:
    print(d[key], end = " ")
