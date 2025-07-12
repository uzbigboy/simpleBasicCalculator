# <----- Creating a funuction to calculate a + b ----->
def add(a, b):
    return a + b

# <----- Creating a funuction to calculate a - b ----->
def munus(a, b):
    return a - b

# <----- Creating a funuction to calculate a * b ----->
def multiply(a, b):
    return a * b

# <----- Creating a funuction to calculate a / b ----->
def devide(a, b):
    return a / b


# <----- Creating a funuction to ask user for a and b ----->
def ask_for_nums():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        return a, b

    # <----- Handling the ValueError, in case user enteres string or emty-string ----->
    except ValueError:
            print("ONLY NUMBERS are allowed")
            return ask_for_nums()


# <----- Creating a funuction to ask user for operator (+, -, *, /) ----->
def ask_for_oper():
    try:
        print("------- Which operation you'd like to do on this numbers? -------\n1.Add(+)\n2.Minus(-)\n3.Multiply(*)\n4.Devide(/)")
        choice = int(input("Enter your choice: "))

        # <----- Raising the ValueError if user inputs a number not listed in the options -----> 
        if choice < 1 or choice > 4:
                raise ValueError
        
        return choice

    # <----- Handling the ValueError -----> 
    except:
        print("enter the NUMBER of operation")
        return ask_for_oper()


# <----- Creating a main function ----->
def main():

    # <----- Creating a loop for multiple using ----->
    while True:
        print("-------- Welcome to simple calculator --------")

        # <----- Calling values for a, b, and choice  ----->
        a, b = ask_for_nums()
        choice = ask_for_oper()

        # <----- Giving an answer according to an operator -----> 
        if choice == 1:
                print(add(a, b))
                
        elif choice == 2:
                print(munus(a, b))

        elif choice == 3:
                print(multiply(a, b))

        elif choice == 4:
            try:
                print(devide(a, b))

            # <----- Handling the ZeroDivisionError if user enters zero(0) as a dividor -----> 
            except ZeroDivisionError:
                print("you CANNOT divide the numers by ZERO")


# <----- Running main function -----> 
main()