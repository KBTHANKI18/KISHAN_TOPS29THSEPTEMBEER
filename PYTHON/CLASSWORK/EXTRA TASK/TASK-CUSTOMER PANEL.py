#customer panel
products = {
    'kiwi': {'qty': 20, 'price': 220},
    'apple': {'qty': 50, 'price': 150}
}
cart = {}
while True:
    print("Product List:")
    for product_name, details in products.items():
        print(f"{product_name.capitalize()}\t{details['qty']}\tRs. {details['price']} per box")

    print("-" * 50)
    product_name = input("Enter product name: ").lower()
    qty = int(input("Qty: "))
    price = products[product_name]['price']
    total_price = price * qty
    print(f"Total Price = Rs. {price} * {qty} = {total_price}\n")
    if product_name in cart:
        cart[product_name] += qty
    else:
        cart[product_name] = qty
    choice = input("Do you want to purchase more products? (y/n): ")
    if choice.lower() == "n":
        break

    print("-" * 50)
print("-" * 50)
print("Cart:")
total_cost = 0
for product_name, qty in cart.items():
    price = products[product_name]['price']
    cost = price * qty
    total_cost += cost
    print(f"{product_name.capitalize()}\t{qty}\tRs. {cost}")
print(f"Total = {total_cost} Rs.")
