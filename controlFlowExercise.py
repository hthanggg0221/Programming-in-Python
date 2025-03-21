num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

for i in num_list:
    print(i, end=" ")
print()

for i in num_list:
    if i > 45:
        print(i, end=" ")
print()

for i in num_list:
    if i > 45:
        print("Over 45")
    else:
        print("Under 45")

for idx, i in enumerate(num_list):
    if i == 36:
        print('Number found at position:', idx)

count = 0
for idx, i in enumerate(num_list):
    count += 1
    if i == 36:
        print('Number found at position:', idx)
        break
