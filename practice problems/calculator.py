def calculator():
    print("Simple Calculator")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Modulus")
    print("7. Exponentiation")
    
    choice = input("Enter choice (1-7): ")
    
    if choice in ['1', '2', '3', '4', '5', '6', '7']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == '1':
            print(f"Result: {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        elif choice == '5':
            if num2 != 0:
                print(f"Result: {num1 // num2}")
            else:
                print("Error: Division by zero is not allowed.")
        elif choice == '6':
            print(f"Result: {num1 % num2}")
        elif choice == '7':
            print(f"Result: {num1 ** num2}")
    else:
        print("Invalid choice! Please enter a number between 1 and 7.")

calculator()
