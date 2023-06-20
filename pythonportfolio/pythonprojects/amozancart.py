import random

cart = []
cart_prices = []
options = ["1. Add an item to your cart", "2. Display your cart", "3. Remove an item from your cart", "4. Checkout", "5: Quit"]
new_item = ""
new_price = 0
stop_menu = False
special_gift = False

print("Welcome to Amozan~ ")
print()
while not stop_menu:
    item_number = 0
    print("~~~ MAIN MENU ~~~")
    print("Would you like to: ")
    for option in options:
        print(option)
    choice = input("")

    if choice == "1":
        main_menu = False
        while not main_menu:
            new_item = input("\nWhat item would you like to add? ")
            new_price = float(input(f"What is the price of '{new_item}'? "))
            print()
            print(f"'{new_item}' has been added to the cart. ")
            cart.append(new_item)
            cart_prices.append(new_price)
            print()
            add_another = input("Would you like to add another item? (yes/no) ")
            while add_another.lower() != "yes" and add_another.lower() != "no":
                print("Please enter 'yes' or 'no' ")
                add_another = input("Would you like to add another item? (yes/no) ")
            if add_another.lower() == "no":
                print()
                main_menu = True

    elif choice == "2":
        item_number = 0
        total = float(sum(cart_prices))
        print("\nYour cart: ")
        for i in range(len(cart)):
            item_number += 1
            item = cart[i]
            item = item.upper()
            price = cart_prices[i]
            print(f"{item_number}. {item} - ${price:.2f}")
        print(f"Total: ${total:.2f}\n")
        delay_menu = input("Press Enter to return to the main menu. ")
        print()
        main_menu = True

    elif choice == "3":
        main_menu = False
        while not main_menu:
            item_number = 0
            total = float(sum(cart_prices))
            print("\nYour cart: ")
            for i in range(len(cart)):
                item_number += 1
                item = cart[i]
                item = item.upper()
                price = cart_prices[i]
                print(f"{item_number}. {item} - ${price:.2f}")
            print(f"Total: ${total:.2f}\n")
            print("If you do not wish to remove an item, enter 'none'")
            item_removal = input("Which item would you like to remove? ")
            if item_removal.lower() == "none":
                main_menu = True
            else:
                item_removal = int(item_removal)
                while item_removal > item_number or item_removal <= 0:
                    print("\nPlease enter the number of the item you wish to remove. ")
                    item_removal = int(input("Which item would you like to remove? "))
                item_removal -= 1
                print(f"\n{cart[item_removal].upper()} has been removed from your cart.")
                cart.pop(item_removal)
                cart_prices.pop(item_removal)
                stop_removal = input("Would you like to remove another item? (yes/no) ")
                while stop_removal.lower() != "yes" and stop_removal.lower() != "no":
                    print("Please enter 'yes' or 'no' ")
                    stop_removal = input("Would you like to remove another item? (yes/no) ")
                if stop_removal.lower() == "no":
                    print()
                    main_menu = True

    elif choice == "4":
        main_menu = False
        while not main_menu:
            item_number = 0
            total = float(sum(cart_prices))
            shipping = float(len(cart)*1.5)
            print("\nYour cart: ")
            for i in range(len(cart)):
                item_number += 1
                item = cart[i]
                item = item.upper()
                price = cart_prices[i]
                print(f"{item_number}. {item} - ${price:.2f}")
            print(f"Total before shipping: ${total:.2f}")
            print(f"Shipping: ${shipping}")
            print(f"Total: ${total+shipping:.2f}\n")
            stop_checkout = input("Would you like to checkout with these items? (yes/no) ")
            while stop_checkout.lower() != "yes" and stop_checkout.lower() != "no":
                print("Please enter 'yes' or 'no' ")
                stop_checkout = input("Would you like to checkout with these items? (yes/no) ")
            if stop_checkout == "yes":
                print("\nThank you for shopping with Amozan! ")
                print(f"Your order of: ", end="")
                for item in cart:
                    item = item.upper()
                    print(item, end=", ")
                print("and a big thanks from us will arrive within 2-100 business days! ")
                main_menu = True
                stop_menu = True
            else:
                print()
                main_menu = True

    
    elif choice == "5":
        for_sure = input("Are you sure you would like to quit? (yes/no) ")
        while for_sure.lower() != "yes" and for_sure.lower() != "no":
                print("Please enter 'yes' or 'no' ")
                for_sure = input("Are you sure you would like to quit? (yes/no) ")
        if for_sure == "yes":    
            stop_menu = True
    
    elif choice == "6":
        if not special_gift:
            special_gift = True
            print("~~You found me!! Just for you, we'll throw in a special something!\n")
            number = random.randint(1,4)
            if number == 1:
                cart.append("Golden Toilet")
                cart_prices.append(0.00)
            elif number == 2:
                cart.append("Deoderant")
                cart_prices.append(0.00)
            elif number == 3:
                cart.append("Spoiled Milk")
                cart_prices.append(0.00)
            elif number == 4:
                cart.append("The One Piece")
                cart_prices.append(0.00)
        else:
            print("Sorry, only one special gift at a time!\n")
        

    else:
        print("Please enter a number between 1 and 4.\n")

if stop_menu:
    print("Please shop with us again soon!\n")