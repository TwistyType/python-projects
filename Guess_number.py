import random
comp_num = random.randint(1,20)

user_name = input("Hello! What is your name?\n")
print("Well " + user_name + ", I am thinking of a number between 1 and 20.")
guesses_taken=1
while(guesses_taken<=6):
    guess = int(input("Take a guess.\n"))
    if guess==comp_num:
        print("Good job, " + user_name + "! You guessed my number in " + str(guesses_taken) + " guesses.")
        break
    else:
        if(guess>comp_num):
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
    guesses_taken+=1

if guess!=comp_num:
    print("Sorry! But the number I was thinking of was " + str(comp_num))
    
            


