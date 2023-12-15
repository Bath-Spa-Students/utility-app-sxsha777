print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print('''
░█▀▀▀█ ─█▀▀█ ▀█▀ █ ░█▀▀▀█ 　 ░█──░█ ░█▀▀▀ ░█▄─░█ ░█▀▀▄ ▀█▀ ░█▄─░█ ░█▀▀█ 　 ░█▀▄▀█ ─█▀▀█ ░█▀▀█ ░█─░█ ▀█▀ ░█▄─░█ ░█▀▀▀ █ 
─▀▀▀▄▄ ░█▄▄█ ░█─ ─ ─▀▀▀▄▄ 　 ─░█░█─ ░█▀▀▀ ░█░█░█ ░█─░█ ░█─ ░█░█░█ ░█─▄▄ 　 ░█░█░█ ░█▄▄█ ░█─── ░█▀▀█ ░█─ ░█░█░█ ░█▀▀▀ ▀ 
░█▄▄▄█ ░█─░█ ▄█▄ ─ ░█▄▄▄█ 　 ──▀▄▀─ ░█▄▄▄ ░█──▀█ ░█▄▄▀ ▄█▄ ░█──▀█ ░█▄▄█ 　 ░█──░█ ░█─░█ ░█▄▄█ ░█─░█ ▄█▄ ░█──▀█ ░█▄▄▄ ▄''')
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Welcome
print("\n")
print("Welcome to my Vending Machine!!")
print("\n")

#Display Categories
print("Vending Machine: Available items")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Category ID    \t", "item Name   \t")
print("1          \t", "Coffee")
print("2          \t", "Energy Drinks")
print("3          \t", "Biscuits")
print("4          \t", "Chocolates")
print("5          \t", "Chips")
print("6          \t", "Fruits")
print("7          \t", "Sandwiches")

print("\n")

order = []
sum = 0
run = True

#Coffee (Function)
def coffee_menu():
    print("Coffee: Menu")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("item ID \t", "item Name   \t", "Price")
    print("711       \t", "Cappuccino \t", 2.00)
    print("712       \t", "Espresso   \t", 2.50)
    print("713       \t", "Latte      \t", 1.50)
    print("714       \t", "Americano  \t", 3.75)
    print("715       \t", "Spanish Latte\t", 2.25)
    print("716       \t", "Iced Coffee\t", 3.00)
    print("717       \t", "Frappe     \t", 2.75)
    print("\n")

    global sum
    global run
    while run:
            ch = int(input("Enter item ID: "))
            if ch == 711:
                print("One Cappuccino is being prepared..")
                order.append("Cappuccino")
                sum = sum + 2.00
            elif ch == 712:
                print("One Epresso is being prepared..")
                order.append("Espresso")
                sum = sum + 2.50 
            elif ch == 713:
                print("One Latte is being prepared..")
                order.append("Latte")
                sum = sum + 1.50
            elif ch == 714:
                print("One Americano is being prepared..")
                order.append("Americano")
                sum = sum + 3.75
            elif ch == 715:
                print("One Spanish Latte is being prepared..")
                order.append("Spanish Latte")
                sum = sum + 2.25
            elif ch == 716:
                print("One Iced Coffee is being prepared.")
                order.append("Iced Coffee")
                sum = sum + 3.00
            elif ch == 717:
                print("One Frappe is being prepared..")
                order.append("Frappe")
                sum = sum + 2.75
            elif ch<711 or ch>717:
                print("ID is invalid.")
                print("Please enter the correct item ID")
    
            print("\n")
            print("Would you like to order more items? Y/N")
            y_n = input("Enter your choice: ")
            if y_n == "N" or y_n == "n":

                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Order Total: ", sum)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                break

#Energy Drinks (Function)
def ed_menu():
    print("Energy Drinks: Menu")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("item ID \t", "item Name   \t", "Price")
    print("718       \t", "Monster   \t", 3.00)
    print("719       \t", "Cola      \t", 2.25)
    print("720       \t", "Sprite    \t", 3.50)
    print("721       \t", "Red Bull  \t", 2.00)
    print("722       \t", "Mountain Dew\t", 1.75)
    print("723       \t", "Fanta     \t", 1.50)
    print("724       \t", "Sway      \t", 2.00)
    print("\n")

    global sum
    global run
    while run:
            ch = int(input("Enter item ID: "))
            if ch == 718:
                print("One can of Monster is being dispensed..")
                order.append("Monster")
                sum = sum + 3.00
            elif ch == 719:
                print("One can of Cola is being dispensed..")
                order.append("Cola")
                sum = sum + 2.25 
            elif ch == 720:
                print("One can of Sprite is being dispensed..")
                order.append("Sprite")
                sum = sum + 3.50
            elif ch == 721:
                print("One can of Red Bull is being dispensed..")
                order.append("Red Bull")
                sum = sum + 2.00
            elif ch == 722:
                print("One can of Mountain Dew is being dispensed..")
                order.append("Mountain Dew")
                sum = sum + 1.75
            elif ch == 723:
                print("One can of Fanta is being dispensed..")
                order.append("Fanta")
                sum = sum + 1.50
            elif ch == 724:
                print("One can of Sway is being dispensed..")
                order.append("Sway")
                sum = sum + 2.00
            elif ch<718 or ch>724:
                print("ID is invalid.")
                print("Please enter the correct item ID")
    
            print("\n")
            print("Would you like to order more items? Y/N")
            y_n = input("Enter your choice: ")
            if y_n == "N" or y_n == "n":

                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Order Total: ", sum)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                break

#Biscuits (Function)
def biscuits_menu():
    print("Biscuits: Menu")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("item ID \t", "item Name       \t", "Price")
    print("725       \t", "Oreo            \t", 1.00)
    print("726       \t", "Loackers        \t", 3.00)
    print("727       \t", "Choco-chip cookie\t", 2.50)
    print("\n")

    global sum
    global run
    while run:
            ch = int(input("Enter item ID: "))
            if ch == 725:
                print("One packet of Oreo is being dispensed..")
                order.append("Oreo")
                sum = sum + 1.00
            elif ch == 726:
                print("One packet of Loackers is being dispensed..")
                order.append("Loackers")
                sum = sum + 3.00 
            elif ch == 727:
                print("One packet of Choco-chip cookie is being dispensed..")
                order.append("Choco-chip cookie")
                sum = sum + 2.50
            elif ch<725 or ch>727:
                print("ID is invalid.")
                print("Please enter the correct item ID")
    
            print("\n")
            print("Would you like to order more items? Y/N")
            y_n = input("Enter your choice: ")
            if y_n == "N" or y_n == "n":

                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Order Total: ", sum)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                break

#Chocolates (Function)
def choco_menu():
    print("Chocolates: Menu")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("item ID \t", "item Name   \t", "Price")
    print("728       \t", "Galaxy    \t", 3.00)
    print("729       \t", "Snickers  \t", 2.00)
    print("730       \t", "Hersheys  \t", 4.50)
    print("731       \t", "Reese     \t", 3.25)
    print("732       \t", "Mars      \t", 2.50)
    print("\n")

    global sum
    global run
    while run:
            ch = int(input("Enter item ID: "))
            if ch == 728:
                print("One Galaxy Chocolate is being dispensed..")
                order.append("Galaxy")
                sum = sum + 3.00
            elif ch == 729:
                print("One Snickers Chocolate is being dispensed..")
                order.append("Snickers")
                sum = sum + 2.00 
            elif ch == 730:
                print("One Hersheys Chocolate is being dispensed..")
                order.append("Hersheys")
                sum = sum + 4.50
            elif ch == 731:
                print("One Reese Chocolate is being dispensed..")
                order.append("Reese")
                sum = sum + 3.25
            elif ch == 732:
                print("One Mars Chocolate is being dispensed..")
                order.append("Mars")
                sum = sum + 2.50
            elif ch<728 or ch>732:
                print("ID is invalid.")
                print("Please enter the correct item ID")
    
            print("\n")
            print("Would you like to order more items? Y/N")
            y_n = input("Enter your choice: ")
            if y_n == "N" or y_n == "n":

                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Order Total: ", sum)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                break

#Chips (Function)
def chips_menu():
    print("Chips: Menu")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("item ID \t", "item Name   \t", "Price")
    print("733       \t", "Lays      \t", 1.00)
    print("734       \t", "Cheetos   \t", 1.50)
    print("735       \t", "Pringles  \t", 3.25)
    print("736       \t", "Doritos   \t", 2.75)
    print("737       \t", "Mr.Krisps.\t", 1.75)
    print("\n")

    global sum
    global run
    while run:
            ch = int(input("Enter item ID: "))
            if ch == 733:
                print("One packet of Lays is being dispensed..")
                order.append("Lays")
                sum = sum + 1.00
            elif ch == 734:
                print("One packet of Cheetos is being dispensed..")
                order.append("Cheetos")
                sum = sum + 1.50 
            elif ch == 735:
                print("One packet of Pringles is being dispensed..")
                order.append("Pringles")
                sum = sum + 3.25
            elif ch == 736:
                print("One packet of Doritos is being dispensed..")
                order.append("Doritos")
                sum = sum + 2.75
            elif ch == 737:
                print("One packet of Mr.Krisps is being dispensed..")
                order.append("Mr.Krisps.")
                sum = sum + 1.75
            elif ch<733 or ch>737:
                print("ID is invalid.")
                print("Please enter the correct item ID")

            print("\n")
            print("Would you like to order more items? Y/N")
            y_n = input("Enter your choice: ")
            if y_n == "N" or y_n == "n":

                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Order Total: ", sum)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                break

#Fruits (Function)
def fruits_menu():
    print("Fruits: Menu")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("item ID \t", "item Name           \t", "Price")
    print("738       \t", "Sliced Watermelon \t", 3.50)
    print("739       \t", "Strawberries      \t", 4.00)
    print("740       \t", "Blueberries       \t", 4.00)
    print("741       \t", "Sliced Pineapple  \t", 5.00)
    print("742       \t", "Sliced Apple      \t", 3.00)
    print("\n")

    global sum
    global run
    while run:
            ch = int(input("Enter item ID: "))
            if ch == 738:
                print("One cup of Sliced Watermelon is being dispensed..")
                order.append("Sliced Watermelon")
                sum = sum + 3.50
            elif ch == 739:
                print("One cup of Strawberries is being dispensed..")
                order.append("Strawberries")
                sum = sum + 4.00 
            elif ch == 740:
                print("One cup of Blueberries is being dispensed..")
                order.append("Blueberries")
                sum = sum + 4.00
            elif ch == 741:
                print("One cup of Sliced Pineapple is being dispensed..")
                order.append("Sliced Pineapple")
                sum = sum + 5.00
            elif ch == 742:
                print("One cup of Sliced Apple is being dispensed..")
                order.append("Sliced Apple")
                sum = sum + 3.00
            elif ch<738 or ch>742:
                print("ID is invalid.")
                print("Please enter the correct item ID")
    
            print("\n")
            print("Would you like to order more items? Y/N")
            y_n = input("Enter your choice: ")
            if y_n == "N" or y_n == "n":

                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Order Total: ", sum)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                break

#Sandwiches (Function)
def sw_menu():
    print("Sandwiches: Menu")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("item ID \t", "item Name          \t", "Price")
    print("743       \t", "Veg Sandwich     \t", 5.00)
    print("744       \t", "Grilled Cheese   \t", 4.50)
    print("745       \t", "Nutella Sandwich \t", 3.00)
    print("746       \t", "Egg Sandwich     \t", 4.75)
    print("747       \t", "Ham Sandwich     \t", 5.00)
    print("\n")

    global sum
    global run
    while run:
            ch = int(input("Enter item ID: "))
            if ch == 743:
                print("One Veg Sandwich is being dispensed..")
                order.append("Veg Sandwich")
                sum = sum + 5.00
            elif ch == 744:
                print("One Grilled Cheese Sandwich is being dispensed..")
                order.append("Grilled Cheese")
                sum = sum + 4.50 
            elif ch == 745:
                print("One Nutella Sandwich is being dispensed..")
                order.append("Nutella Sandwich")
                sum = sum + 3.00
            elif ch == 746:
                print("One Egg Sandwich is being dispensed..")
                order.append("Egg Sandwich")
                sum = sum + 4.75
            elif ch == 747:
                print("One Ham Sandwich is being dispensed..")
                order.append("Ham Sandwich")
                sum = sum + 5.00
            elif ch<743 or ch>747:
                print("ID is invalid.")
                print("Please enter the correct item ID")
    
            print("\n")
            print("Would you like to order more items? Y/N")
            y_n = input("Enter your choice: ")
            if y_n == "N" or y_n == "n":

                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Order Total: ", sum)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                break

#Payment (Function)
def ord_payment():
    global sum
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Your Order: ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in order:
        print(i)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Order total: ", sum)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if sum>0:
        print("Would you like to pay in cash or card?")
        mode=input("Enter mode of payment: ")
        if mode == "card":
            amt = float(input("Enter amount to be paid: "))
            print("Processing...")
            print("Transaction complete!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Thank you!! Please visit us again!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        elif mode == "cash":
            amt = int(input("Enter the amount: "))
            change = 0
            if amt == sum:
                print("Paid!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Thank you!! Please visit us again!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            else:
                    change = amt - sum
                    print("Change: ", change)
                    print("Please collect you change in the slot below.")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Thank you!")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            print("Mode of payment is invalid. Please try again..")

#Vending Machine Logic
while True:
    cat = input("Enter the category you would like to browse (None to proceed to payment): ")
    if cat == "coffee":
        coffee_menu()
    elif cat == "energy drinks":
        ed_menu()
    elif cat == "biscuits":
        biscuits_menu()
    elif cat == "chocolates":
        choco_menu()
    elif cat == "chips":
        chips_menu()
    elif cat == "fruits":
        fruits_menu()
    elif cat == "sandwiches":
        sw_menu()
    elif cat == "None":
        ord_payment()
        break
    else:
        print("Invalid category")