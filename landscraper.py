def cut_grass_with_teeth(earnings):
    earnings += 1
    print("You used your teeth to cut grass and earned $1.")
    return earnings

def buy_rusty_scissors(earnings, has_scissors):
    if not has_scissors and earnings >= 5:
        earnings -= 5
        has_scissors = True
        print("You bought a pair of rusty scrissors")
    else:
        print("You either already have scissors or don't have enough money")
    
    return earnings, has_scissors

def display_earnings(earnings):
    print(f"Total earnings: ${earnings}")

def main():
    earnings = 0
    has_scissors = False

    while True:
        print("1. Use teeth to cut grass and earn $1")
        print("2. Buy rusty scrissors for $5")
        print("3. Display total earnings")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            earnings = cut_grass_with_teeth(earnings)
        elif choice == "2":
            earnings, has_scissors = buy_rusty_scissors(earnings, has_scissors)
        elif choice == "3":
            display_earnings(earnings)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
