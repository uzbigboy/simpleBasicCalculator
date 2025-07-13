# <----- Creating a function to calculate a + b ----->
def add(a, b):
    return a + b


# <----- Creating a function to calculate a - b ----->
def subtract(a, b):
    return a - b


# <----- Creating a function to calculate a * b ----->
def multiply(a, b):
    return a * b


# <----- Creating a function to calculate a / b ----->
def divide(a, b):
    return a / b


# <----- Creating a function to ask user for a and b ----->
def ask_for_nums():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        return a, b

    # <----- Handling the ValueError, in case user enters string or empty string ----->
    except ValueError:
        print("ONLY NUMBERS are allowed")
        return ask_for_nums()


# <----- Creating a function to ask user for operator (+, -, *, /) ----->
def ask_for_oper():
    try:
        print("------- Which operation would you like to do on these numbers? -------\n1.Add(+)\n2.Subtract(-)\n3.Multiply(*)\n4.Divide(/)")
        choice = int(input("Enter your choice: "))

        # <----- Raising the ValueError if user inputs a number not listed in the options -----> 
        if choice < 1 or choice > 4:
            raise ValueError
        
        return choice

    # <----- Handling the ValueError -----> 
    except ValueError:
        print("Enter the NUMBER of the operation (1-4)")
        return ask_for_oper()


# <----- Creating a main function ----->
def main():

    # <----- Creating a loop for multiple uses ----->
    while True:
        print("-------- Welcome to the simple calculator --------")

        # <----- Calling values for a, b, and choice  ----->
        a, b = ask_for_nums()
        choice = ask_for_oper()

        # <----- Giving an answer according to the operator ----->
        if choice == 1:
            print(add(a, b))
        elif choice == 2:
            print(subtract(a, b))
        elif choice == 3:
            print(multiply(a, b))
        elif choice == 4:
            try:
                print(divide(a, b))

            # <----- Handling the ZeroDivisionError if user enters zero(0) as a divisor -----> 
            except ZeroDivisionError:
                print("You CANNOT divide numbers by ZERO")


# <----- Running main function ----->
main()
