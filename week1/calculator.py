def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b

def main():
    print("Basic Calculator (+, -, *, /)")
    try:
        a = float(input("Enter first number: "))
        op = input("Operator (+,-,*,/): ").strip()
        b = float(input("Enter second number: "))
        ops = {"+": add, "-": sub, "*": mul, "/": div}
        if op in ops:
            if op == "/" and b == 0:
                print("Error: Division by zero.")
            else:
                print("Result:", ops[op](a,b))
        else:
            print("Unsupported operator.")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()