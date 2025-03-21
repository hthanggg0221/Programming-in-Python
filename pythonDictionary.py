my_d = {1: 'Test', "Name": "Epilogue", 1: 'Not test'}

print(my_d)
print(my_d[1])
print(my_d['Name'])

my_d[2] = 'Test 2'
my_d[1] = 'Not a test!'
print(my_d)

del my_d[2]
print(my_d)

for x in my_d:
    print(x)

for key, value in my_d.items():
    print(str(key) + ": " + value)