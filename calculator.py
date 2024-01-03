

#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#divide
def divide(n1, n2):
    return n1 / n2

#multiply
def multiply(n1, n2):
    return n1 * n2

def calculator():
    num1 = float(input('Enter the first number: '))



    operations = {
        "+" : add,
        "-" : subtract,
        "/" : divide,
        "*" : multiply
    }

    for symbol in operations:
        print(symbol)
    continue_calc = True
    while continue_calc:
        operator = input('Pick an operation: ')

        n2 = float(input('Enter the second number: '))
        result_n = operations[operator]
        result = result_n(num1, n2)
        print(f'{num1} {operator} {n2} = {result}')
        
        
        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit. :") == 'y':
            num1 = result
            
        else:
            continue_calc = False
            calculator()
calculator()
                    