def calculateTax(bill, taxRate):
    return round((bill * taxRate) / 100.00, 2)

print('Total tax:', calculateTax(175.00, 15))

print('Total tax:', calculateTax(164.33, 22))