my_list = [1,2,3]

def add_to_list(item):
    nl = my_list.copy()
    nl.append(item)
    return nl

new_list = add_to_list(4)

print(my_list)
print(new_list)