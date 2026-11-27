import random 


answer = "Y"

while answer == "Y":
    myNumber = random.randint(1,100)

    
    guessNumber = 0
    count = 0 
    guessLimit = 10


    while myNumber != guessNumber:

        if count == guessLimit:
            print("You have reached guess limit")
            print(f"The number was {myNumber}")
            answer = input("Do you want to play again: Y or N: ").upper()
            break

        try:
            guessNumber = int(input("Enter a number: "))
        except:
            print("Invalid number!")
            continue

        if myNumber > guessNumber:
            print("My number is greater than your number")
            count += 1
        elif myNumber < guessNumber:
            print("My number is less than your number")
            count += 1
        else:
            print(f"You found the number after {count} times")
            print(myNumber)
            answer = input("Do you want to play again: Y or N: ").upper()
            break         
