import random


def guess():
    number = random.randint(1,10)
    count =1
    while count <=3:
        choice = int(input("Enter your choice(1- 10): "))
        if number == choice:
            print('you win')
            break

        else:
            if count ==3:
                print(f'You loss.The number is {number}')
                break
            else:
                print(f'you loss.try {3-count} more time')
                count += 1
                if choice <number:
                    print("Yor choice is low")
                else:
                    print("your choice is high")

guess()