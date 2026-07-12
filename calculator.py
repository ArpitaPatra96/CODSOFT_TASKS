print("=" * 25)
print(" SIMPLE CALCULATOR")
print("=" * 25)

while True:
    first_number = float(input("Enter First Number : "))
    second_number = float(input("Enter Second Number : "))

    print("\nChoose an Operation")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        answer = first_number + second_number
        print(f"\nResult = {answer}")

    elif choice == "2":
        answer = first_number - second_number
        print(f"\nResult = {answer}")
    elif choice == "3":
        answer = first_number * second_number
        print(f"\nResult = {answer}")
    elif choice == "4":
        if second_number == 0:
            print("\nError ! Division by zero is not possible.")
        else:
            answer = first_number / second_number
            print(f"\nResult = {answer}")
    else:
        print("\nInvalid Choice!")

    again = input("\nDo you want to calculate again? (yes/no): ").lower()

    if again != "yes":
        print("\nThank you for using Simple Calculator!")
        break





      