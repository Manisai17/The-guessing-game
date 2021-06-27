import random
print("Welcome to Guessing Game!!!")
print("We can guess the number in your mind :) ")
print("Do you want to play the game(if yes, enter y)? : ")
ans = input()
if ans == "y":
    print("Let's start the game!!!")
    print("The Rules of the game are: \n "
          "1. y = YES and any keyword = NO \n "
          "2. You can simply exit the game by pressing any keyword other than y at any moment if you want to leave. \n "
          "3. After performing the calculations in your mind you can respond me with y")
    print("Now choose a number in your mind.")
    if input() == "y":
        print("Now multiply the number with 2")
        if input() == "y" :
            num = random.randrange(10,100,10)
            print("Now add", num ,"to your answer")
            if input() == "y" :
                print("Now divide your answer by 2")
                if input() == "y" :
                    print("Now subtract the number that you have assumed in your mind")
                    if input() == "y" :
                        print("Your answer is:" , int(num/2) )
else:
    print("Come back again!!!")
