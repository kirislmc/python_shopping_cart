print("Welcome to the Shop!")
shopping_cart = []
response = input("Would you like to add something to your cart? y/n: ").lower()

while True:

   if response == "y":
       item = input("What would you like to add to your cart?: ").lower()
       print(f"You have now put {item.capitalize()} in your cart!")
       shopping_cart.append(item)
   else:
       print("Thank you for shopping!")
       break

   while True:
       response = input("Would you like to remove anything from your cart? y/n: ").lower()
       if response == "y":
           removed_item = input("What would you like to remove?: ").lower()
           if removed_item in shopping_cart:
               shopping_cart.remove(removed_item)
               break
           else:
               print(f"{removed_item.capitalize()} is not in your cart!")
       else:
           break

   response = input("Would you like to keep shopping? y/n: ").lower()
   if response == "n":
       print("Thank you for shopping with us!")
       break

print(shopping_cart)