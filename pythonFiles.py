try:
    with open('newFile.txt', 'a') as file:
        file.write("This is a new file created!")
        file.writelines(["\nHello @everyone!", "\nThis is another line to be added."])
except FileNotFoundError as e:
    print("ERROR!", e)
