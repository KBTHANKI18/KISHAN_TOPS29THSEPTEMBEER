GOLD_PRICE_PER_GRAM = 5752
MAKING_CHARGES_PER_GRAM = 845

def calculate_gold_rate(gram):
    return GOLD_PRICE_PER_GRAM * gram

def calculate_making_charges(gold_rate):
    return MAKING_CHARGES_PER_GRAM * gold_rate

def calculate_discount(age, gender, purchase_amount):
    discount = 0
    if gender == 'M':
        if age >= 65:
            if purchase_amount > 500000:
                discount = 0.35
            elif purchase_amount > 300000:
                discount = 0.3
            elif purchase_amount > 200000:
                discount = 0.2
        else:
            if purchase_amount > 500000:
                discount = 0.25
            elif purchase_amount > 300000:
                discount = 0.2
            elif purchase_amount > 200000:
                discount = 0.1
    elif gender == 'F':
        if age >= 65:
            if purchase_amount > 500000:
                discount = 0.4
            elif purchase_amount > 300000:
                discount = 0.35
            elif purchase_amount > 200000:
                discount = 0.25
        else:
            if purchase_amount > 500000:
                discount = 0.3
            elif purchase_amount > 300000:
                discount = 0.25
            elif purchase_amount > 200000:
                discount = 0.15
    return discount


name = input("Enter your name: ")
gender = input("Enter your gender (M/F): ")
age = int(input("Enter your age: "))
product = input("Enter product: ")
gram = float(input("Enter product gram: "))
gold_rate = calculate_gold_rate(gram)
print("-------------------------------------------")
print("TOTAL GOLD RATE : ", gold_rate)
making_charges = calculate_making_charges(gold_rate)
print("Making charges (1 gram)  : ", MAKING_CHARGES_PER_GRAM)
print("Total Making Charges :   ", making_charges)
total_amount = gold_rate + making_charges
print("-------------------------------------------")
print("TOTAL AMOUNT : ", total_amount)
discount = calculate_discount(age, gender, total_amount)
discount_amount = total_amount * discount
print("DISCOUNT : ", discount * 100, "%")
print("DIS- AMOUNT : ", discount_amount)
net_amount = total_amount - discount_amount
print("--------------------------------------------")
print("total net amount : ", net_amount)
print("--------------------------------------------")