def add(a, b):
    return a + b

def munus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def devide(a, b):
    return a / b

def asking_user_for_nums():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

    except ValueError:
            print("ONLY NUMBERS ARE ALLOWED")
            asking_user_for_nums()

def main():
    while True:
        print("-------- Welcome to simple calculator --------")

        asking_user_for_nums()

        print("------- Which operation you'd like to do on this numbers? -------\n1.Add(+)\n2.Minus(-)\n3.Multiply(*)\n4.Devide(/)")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(add(a, b))
        elif choice == 2:
            print(munus(a, b))
        elif choice == 3:
            print(multiply(a, b))
        elif choice == 4:
            print(devide(a, b))
main()