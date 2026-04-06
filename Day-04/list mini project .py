items = []
prices = []

print(" Welcome to Grocery Billing System")

while True:
    item = input("Enter item (or 'done' to finish): ")

    if item == "done":
        break

    price = float(input("Enter price: "))

    items.append(item)
    prices.append(price)

print("="*20)
print(" BILL")
print("="*20)

total = 0

for i in range(len(items)):
    print(items[i], "=", prices[i])
    total += prices[i]

print("-------------------")
print("Total =", total)

#Enter item: milk
#Enter price: 40
#Enter item: bread
#Enter price: 30
#Enter item: done

#BILL-
milk = 40
bread = 30
Total = 70

#work-flow-User input → store in list → loop → calculate → print
#Enter item: milk
#Enter price: 40
#Enter item: bread
#Enter price: 30
#Enter item: done

#BILL-
milk = 40
bread = 30
Total = 70

#work-flow-User input → store in list → loop → calculate → print