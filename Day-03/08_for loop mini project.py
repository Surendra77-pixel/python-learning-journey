
#lets create the for loop mini project

# 🛒 SHOPPING CART MINI PROJECT

products = [
    {"name": "Shirt", "price": 500},
    {"name": "Shoes", "price": 1500},
    {"name": "Watch", "price": 2000},
    {"name": "Cap", "price": 300}
]

# Show products
print("Available Products:\n")

for i in range(len(products)):
    print(i, "-", products[i]["name"], "₹", products[i]["price"])

# User input
cart = []
choices = input("\nEnter product numbers (comma separated): ")

selected = choices.split(",")

# Add to cart
for item in selected:
    index = int(item)
    cart.append(products[index])

# Calculate total
total = 0

print("\nYour Cart:\n")

for item in cart:
    print(item["name"], "-", item["price"])
    total += item["price"]

print("\nTotal Bill:", total)

#OUTPUT:
#Available Products:
#0 - Shirt ₹ 500
#1 - Shoes ₹ 1500
#2 - Watch ₹ 2000
#3 - Cap ₹ 300
#Enter product numbers (comma separated): 0,2
#Your Cart:
#Shirt - 500
#Watch - 2000
#Total Bill: 2500

#explanation: In this mini project, we have a list of products, each represented as a dictionary with a name and price. We display the available products to the user and prompt them to enter the product numbers they wish to purchase. The user's input is split into a list of selected product indices, which are then used to add the corresponding products to the cart. Finally, we calculate the total bill by iterating through the cart and summing up the prices of the selected products.

while True:
    break
    #means the loop will continue to run indefinitely until we break out of it.