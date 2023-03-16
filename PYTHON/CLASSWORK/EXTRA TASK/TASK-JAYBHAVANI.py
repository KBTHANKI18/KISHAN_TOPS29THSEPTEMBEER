def show_menu(menu):
    print("Menu:")
    for k, v in menu.items():
        print(f"{k} Rs. {v}")

def create_cart(menu):
    cart = {}
    status = True
    while status:
        product_name = str(input("Enter product: "))
        qty = int(input("Enter number of qty: "))
        price = qty * menu[product_name]
        cart[product_name] = price
        choice = input("Do you want to purchase more products? Press y for yes and n for no")
        if choice == 'n' or choice=='N':
            status = False
            break
    return cart

jay_bhavani = {
    "vadapav": 30,
    "dabeli": 20,
    "bhel": 70,
}

show_menu(jay_bhavani)
cart = create_cart(jay_bhavani)
print("Cart:", cart)