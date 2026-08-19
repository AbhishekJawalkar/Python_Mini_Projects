"""

This is a Food Ordering System that takes order from the user based on his/her inputs and showcases final order with the billing amount, it also allows the user to update the order by adding or removing items.

"""
print("#-----------------------------------------------------#")
print("#######################################################")
print("#-----------------------------------------------------#")
print("")
print("           Welcome to Sharlet's Restuarant"            )
print("")
print("#-----------------------------------------------------#")
print("#######################################################")
print("#-----------------------------------------------------#")
print("")
print("What would you like to have today")
print("")
print("Here's the Menu :-")
print("")
print(" 1. Biryani - 300, \n 2. Kebabs - 250, \n 3. Murg Mussallam - 275, \n 4. Steam Rice - 100, \n 5. Roti - 50, \n 6. Shawarma - 150, \n 7. Tandoori Chicken - 260, \n 8. Chatpata Chicken - 200, ")
print("")
print("")
print("Before Ordering, Please enter your information")
print("")
Name = input("Your Good Name : ")
print("")
Contact = int(input("Your Mobile Number(10 Digits) : "))
print("")
print("Thank you for your Information sir, Let me get your order now.")
print("")
print("Enter the order using Serial Numbers of the items. (Keep Spaces)")
print("For Multiple Same items repeat the number again.\n    eg:- For 2 Roti's - 5 5")
print("")
Menu = {
    1:"Biryani", 
    2:"Kebabs", 
    3:"Murg Mussallam", 
    4:"Steam Rice", 
    5:"Roti", 
    6:"Shawarma",
    7:"Tandoori Chicken", 
    8:"Chatpata Chicken"
    }
Prices = {
    1:300,
    2:250,
    3:275,
    4:100,
    5:50,
    6:150,
    7:260,
    8:200
    }
order = list(map(int, input().split()))
while True:
    print("")
    print("Perfect, Let me Repeat your Order")
    print("")
    for item in order:
        print(Menu[item])
    update = input("\nWould you like to add anything to your order? (Y/N): ").upper()
    print("")
    if update == "Y":
        new_items = list(map(int, input("Enter the items you want to add: ").split()))
        order.extend(new_items)
    elif update == "N":
        print("\nThank you! Your order is confirmed.")
        break
    else:
        print("\nPlease enter Y or N.")
print("\n----------------------------------")
print("============== BILL ==============")
print("----------------------------------")
print("")
print(f"Customer Name: {Name}")
print(f"Customer Contact: {Contact}")
print("")
total = 0
for item in order:
    if item in Menu:
        print(f"{Menu[item]} - ₹{Prices[item]}")
        total += Prices[item]
print("")
print("----------------------------------")
print(f"Total Bill: ₹{total}")
print("==================================")
print("")