def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def main():
    print("Temperature Converter")
    print("1) Celsius to Fahrenheit")
    print("2) Fahrenheit to Celsius")
    choice = input("Choose 1 or 2: ").strip()
    try:
        if choice == "1":
            c = float(input("Enter °C: "))
            print("Result:", round(c_to_f(c), 2), "°F")
        elif choice == "2":
            f = float(input("Enter °F: "))
            print("Result:", round(f_to_c(f), 2), "°C")
        else:
            print("Invalid option.")
    except ValueError:
        print("Please enter numeric values only.")

if __name__ == "__main__":
    main()