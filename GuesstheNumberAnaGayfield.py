import random

print("Welcome to the Guessing Game where you will guess a number between the range you will create. \n "
      "The number is inclusive of your entered minimum and maximum")

minimum = int(input("Please Enter a Number for the Minimum:"))
maximum = int(input("Please Enter Another Number for the Maximum:"))

secretnumber = random.randint(minimum, maximum)

def play_game(guess):
                
    while True:
        if guess not in range(minimum, maximum):
            print("Your guess needs to be in your selected range.")
            
        elif guess < secretnumber:
            print("Your guess is too low. Please Guess Higher.")
            
            
            

        elif guess > secretnumber:
            print("Your guess is too high. Please Guess Lower.")
            

            
        else:
            print("You guessed correctly! Congratulations!")
            print(input("Thank you for playing! Consider Playing Again. Now Please Press Enter to Quit:"))
            break
        guess = int(input("Please Guess a Number:"))


            



guess = play_game(int(input("Please Guess a Number:")))
