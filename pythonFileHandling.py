file = open('test.txt', mode = 'r')
data = file.readline()

print(data)
file.close()

with open('test.txt', mode = 'r') as file1:
    data1 = file1.readline()
    print(data1)