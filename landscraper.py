def cut_grass_with_teeth(earnings):
    earnings += 1
    print("You used your teeth to cut grass and earned $1.")
    return earnings

def display_earnings(earnings):
    print(f"Total earnings: ${earnings}")

def main():
    earnings = 0

    while True:
        print("1. Use teeth to cut grass and earn $1")
        print("2. Display total earnings")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            earnings = cut_grass_with_teeth(earnings)
        elif choice == "2":
            display_earnings(earnings)
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
