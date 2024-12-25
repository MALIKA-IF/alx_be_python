import random
secret_number = random.randint(1, 10)
guess = int(input("enter your number " ))

match guess:
    case secret_number:
        print("Congratulations, you guessed it!")
 

