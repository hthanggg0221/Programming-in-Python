list1 = [1, 2, 3, 4, 5]

print(list1[2])
print(*list1)
print(list1, sep=" ")

list1.insert(len(list1), 6)
print(list1, sep=" ")

list1.append(7)
print(list1, sep=" ")

list1.extend([8, 9, 10, 11])
print(list1, sep=" ")

list1.pop(10)
print(list1, sep=" ")

del list1[9]
print(list1, sep=" ")

for x in list1:
    print('Value:', x)

list2 = ['A', 'B', 'C', 'D', 'E']

list3 = ["Hello", 12, True, 37.38]

list4 = [1, [2, 3, 4], 5, 6]