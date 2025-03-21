for i in range(10):
    print("Looping ..", i)

favourites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisu', 'Chocolate Cake']

for item in favourites:
    print("I like this desert", item)

count = 0

while count < len(favourites):
    print("I like this desert", favourites[count])
    count += 1

for idx, item in enumerate(favourites):
    print(idx, item)