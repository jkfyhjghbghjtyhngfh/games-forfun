import sympy

def basic_calculator():
    print("Basic Calculator (type 'exit' to quit)")
    while True:
        expr = input("Enter a mathematical expression (e.g., 2+3*4): ")
        if expr.lower() == "exit":
            break
        try:
            result = eval(expr)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

def algebra_calculator():
    print("Algebra Calculator (type 'exit' to quit)")
    while True:
        expr = input("Enter an algebraic expression (e.g., x**2 + 2*x + 1): ")
        if expr.lower() == "exit":
            break
        try:
            # Parse and simplify the expression
            result = sympy.simplify(expr)
            print(f"Simplified: {result}")
            
            # Optionally, solve expressions with equality (e.g., x**2 = 4)
            if '=' in expr:
                left, right = expr.split('=')
                symbol = sympy.symbols('x')
                solution = sympy.solve(sympy.sympify(left) - sympy.sympify(right), symbol)
                print(f"Solution for x: {solution}")
        except Exception as e:
            print(f"Error: {e}")

def main():
    print("Welcome to the Python Calculator!")
    print("Choose mode:")
    print("1. Basic Math")
    print("2. Algebra")
    choice = input("Enter 1 or 2: ")
    if choice == '1':
        basic_calculator()
    elif choice == '2':
        algebra_calculator()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()