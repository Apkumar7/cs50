user = int(input())

c = user%10

user = user/10

b = round(user%10)


user = user/10

a = round(user%10)


ones = 0

zeros = 0

if a == 1:
    ones += 1
elif a == 0:
    zeros += 1
else:
    pass


if b == 1:
    ones += 1
elif b == 0:
    zeros += 1
else:
    pass


if c == 1:
    ones += 1
elif c == 0:
    zeros += 1
else:
    pass

print(ones)
