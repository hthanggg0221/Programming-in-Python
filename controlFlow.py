billTotal = 210

discount1 = 10
discount2 = 20

if billTotal > 200:
    print("Bill is greater than 200")
    billTotal = billTotal - discount2
elif billTotal > 100:
    print("Bill is greater than 100")
    billTotal = billTotal - discount1
else:
    print("Bill is less than 100")

print("Total bill: {}".format(billTotal))
print("Total bill: " + str(billTotal))