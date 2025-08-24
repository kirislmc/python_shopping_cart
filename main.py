print("Welcome to the Shop!")

response = input("Would you like to add something to your cart? Y/N: ").capitalize()

if response == "Y":
    answer = input("What would you like to add to your cart?: ")
    print(f"You have now put {answer} in your cart!")

    response2 = input("Would you like to remove anything from your cart? Y/N: ").capitalize()

    if response2 == "Y":
        answer2 = input(f"Would you like to remove {answer.lower()}? Y/N: ").capitalize()

        if answer2 == "Y":
            print(f"You have successfully removed {answer}!")
        else:
            print(f"{answer} remains in your cart.")
            print("Thank you for shopping with us!")
    else:
        stay = input("Would you like to keep shopping or leave the shop? S/L: ").capitalize()

        if stay == "S":
            more = input("What would you like to have?: ")
            print(f"{more} has been added to your cart!")
        else:
            print("Thank you for shopping with us!")

            choice = input("Keep shopping or leave? (S/L): ").capitalize()
            if choice == "L":
                print("Thanks for shopping!")
            'break'

else:
    print("Cart empty. Please try again!")

