product_menu = {}

menu = """"
               
                         press 1 for product manager
                         press 2 for customer
                         press 3 for exit

        """ 

status = True
p_status = True
while status:
    print(menu)
    choice = int(input("Enter Your Choice : "))                 
    if choice ==1:
        while p_status:
            __spec_ ={}
            print("Welcome to Product Manager")
            product_name = input("Enter Product Name : ")
            qty = int(input("Enter Qty : "))
            amount = int(input("Enter Amount : "))
            if product_name in product_menu.keys():
                __spec_['qty'] = product_menu[product_name]['qty'] + qty
                __spec_["amount"]=amount
            else:
                __spec_['qty']=qty
                __spec_['amount']=amount

            product_menu[product_name] = __spec_

            print(product_menu)

            p_choice = input("Do you want to add more product? :")
            if p_choice=='n':
                
                p_status = False
    elif choice == 2:
        print("CUSTOMER")
    else:
        print("Thank You For Using This Application")
        status = False                    

