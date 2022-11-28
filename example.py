np = [1, 2, 3, 4, 5]
i = 1
while i < 5:
    np[i] *= np[i-1]
    i += 1
print("using while: " + str(np))

np = [1,2,3,4,5]
for x in range(1,5):
    np[x] *= np[x-1]
print("using for: " + str(np))

print("i made a change - ricky")
