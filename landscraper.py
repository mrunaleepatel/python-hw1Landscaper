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

def cut_grass_with_scissors(earnings):
    earnings += 5
    print("You used the rusty scrissors to cut and earned $5")
    return earnings

def buy_push_lawnmower(earnings, has_scissors, has_lawnmower):
    if not has_scissors and earnings >= 25 and has_scissors:
        earnings -= 25
        has_lawnmower = True
        print("You bought an old push lawnmover")
    else:
        print("You either already have a lawnmower, don't have enough money, or need scissors to buy it")
    
    return earnings, has_lawnmower

def cut_grass_with_lawnmower(earnings):
    earnings += 50
    print("You used the old push lawnmower to cut grass and earned $50.")
    return earnings

def buy_fancy_lawnmower(earnings, has_lawnmower, has_fancy_lawnmower):
    if not has_fancy_lawnmower and earnings >= 250 and has_lawnmower:
        earnings -= 250
        has_fancy_lawnmower = True
        print("You bought a fancy lawnmower!")
    else:
        print("You either already have a fancy lawnmower, don't have enough money, or need an old lawnmower to buy it.")

    return earnings, has_fancy_lawnmower

def cut_grass_with_fancy_lawnmower(earnings):
    earnings += 100
    print("You used the fancy battery-powered lawnmower to cut grass and earned $100.")
    return earnings

def hire_students(earnings, has_fancy_lawnmower, has_students):
    if not has_students and earnings >= 500 and has_fancy_lawnmower:
        earnings -= 500
        has_students = True
        print("You hired a team of starving students!")
    else:
        print("You either already have a team of students, don't have enough money, or need a fancy lawnmower to hire them.")

    return earnings, has_students

def display_earnings(earnings):
    print(f"Total earnings: ${earnings}")

def main():
    earnings = 0
    has_scissors = False
    has_lawnmower = False
    has_fancy_lawnmower = False
    has_students = False

    while True:
        print("1. Use teeth to cut grass and earn $1")
        print("2. Buy rusty scissors for $5")
        print("3. Use rusty scissors to cut grass and earn $5")
        print("4. Buy old push lawnmower for $25")
        print("5. Use lawnmower to cut grass and earn $50")
        print("6. Buy fancy lawnmower for $250")
        print("7. Use fancy lawnmower to cut grass and earn $100")
        print("8. Hire team of starving students for $500")
        print("9. Display total earnings")
        print("10. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            earnings = cut_grass_with_teeth(earnings)
        elif choice == "2":
            earnings, has_scissors = buy_rusty_scissors(earnings, has_scissors)
        elif choice == "3":
            if has_scissors:
                earnings = cut_grass_with_scissors(earnings)
            else:
                print("You need to buy rusty scissors first.")
        elif choice == "4":
            earnings, has_lawnmower = buy_push_lawnmower(earnings, has_scissors, has_lawnmower)
        elif choice == "5":
            if has_lawnmower:
                earnings = cut_grass_with_lawnmower(earnings)
            else:
                print("You need to buy an old push lawnmower first.")
        elif choice == "6":
            earnings, has_fancy_lawnmower = buy_fancy_lawnmower(earnings, has_lawnmower, has_fancy_lawnmower)
        elif choice == "7":
            if has_fancy_lawnmower:
                earnings = cut_grass_with_fancy_lawnmower(earnings)
            else:
                print("You need to buy a fancy lawnmower first.")
        elif choice == "8":
            earnings, has_students = hire_students(earnings, has_fancy_lawnmower, has_students)
        elif choice == "9":
            display_earnings(earnings)
        elif choice == "10":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
