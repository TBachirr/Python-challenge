def Add(n1, n2):
    return n1 + n2

def Substract(n1, n2):
    return n1 - n2

def Multiply(n1, n2):
    return n1 * n2

def Divide(n1, n2):
    return n1 / n2      

operations = {
    "+": Add,
    "-": Substract,
    "*": Multiply,
    "/": Divide
}
def Calculator():
    n1 = float(input("What's the first number?: "))
    should_continue = True
    while should_continue:
        for i in operations:
            print(i)
        operation = input("Pick an operation: ")

        n2 = float(input("What's the second number?: "))

        calculation_function = operations[operation]
        answer = calculation_function(n1, n2)

        print(f"{n1} {operation} {n2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            n1 = answer
        else:
            should_continue = False
            Calculator()
