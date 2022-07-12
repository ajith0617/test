def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

while True :
    print("""
    1) Add
    2) Sub
    3) Mul
    4) Div
    """)
    choice = input("Enter your choice (1,2,3,4): ")
    if choice in ['1','2','3','4']:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if choice == '1':
            print(f"Answer = {add(a,b)}")

        elif choice == '2':
            print(f"Answer = {sub(a,b)}")

        elif choice == '3':
            print(f"Answer = {mul(a,b)}")

        elif choice == '4':
            print(f"Answer = {div(a,b)}")
        
        second_choice = input("Do you want to play again? (Y/N): ").lower()
        if second_choice == 'n':
            break

    else:
        print("Please enter the correct choice")
            
