def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def main():
    print("Welcome to the Temperature Converter!")
    while True:
        print("\nChoose an option:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            try:
                celsius = float(input("Enter the temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius}°C is equal to {fahrenheit}°F")
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
        elif choice == '2':
            try:
                fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit}°F is equal to {celsius}°C")
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
