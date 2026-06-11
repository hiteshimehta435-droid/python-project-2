while True:
    print("Welcome to the Generate Right-Angled Triangle pattern and Analyze Number!")
    print("1. Generate Right-Angled Triangle Pattern")
    print("2. Analyze Numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        rows = int(input("Enter number of rows: "))

        if rows <= 0:
            print("Invalid row count!")
            break

        print("\nRight-Angled Triangle Pattern:")
        for i in range(1, rows + 1):
            print("*" * i)

    elif choice == "2":
        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))

        print("\nNumber Analysis:")

        for num in range(start, end + 1):

            if num == 5:
                pass

            if num % 2 == 0:
                print(num, "- Even")

            elif num % 3 == 0:
                print(num, "- Divisible by 3")

            else:
                print(num, "- Other")

    elif choice == "3":
        print("Program Exited Successfully.")
        print("Thank you")
        print("Have good day")
        break

    else:
        print("Invalid Choice! Try Again.")
