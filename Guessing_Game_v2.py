def Play_Game():
    import random
    import pyfiglet
    import termcolor

    msg = pyfiglet.figlet_format("Welcome to the guessing game!\n Let's start!")
    msg = termcolor.colored(msg, color="magenta", attrs=["blink"])
    print(msg)

    play = "y"
    x = random.randint(1, 10)
    while play == ("y"):
        a = input("Guess a number between 1 to 10\n(Whole numbers only,not decimals and text):  ")
        try:
            a = int(a)
        except:
            print("Please enter an integer")
        else:
            if a > 10:
                print("Invalid entry!!\nThe numbers should be between 1 to 10")
            while a != x:
                if a == x + 1 or a == x - 1:
                    print("Soo close!!!!!!")
                    if a <= x:
                        print("A little more!\nTry again")
                        break
                    if a >= x:
                        print("A little less!\nTry again")
                        break
                elif a == x + 2 or a == x - 2:
                    print("Close, but no.....")
                    if a <= x:
                        print("Your guess is a little low!\nTry again")
                        break
                    if a >= x:
                        print("Your guess is a little high!\nTry again")
                        break
                elif abs(a -x) < 5:
                    print("You are off by quite a bit!")
                    if a <= x:
                        print("Your guess is low!\nTry again")
                        break
                    if a >= x:
                        print("Your guess is high!\nTry again")
                        break
                else:
                    print("You are off by a lot!!")
                    if a <= x:
                        print("Your guess is too low!\nTry again")
                        break
                    if a >= x:
                        print("Your guess is too high!\nTry again")
                        break

            if a == x:
                print("You Guessed It!!")
                play = input("Do You want to play again?(y or n)")
                x = random.randint(1, 10)
    print("Thanks for playing! Bye!!\U0001f600")

if __name__ == "__main__":
    Play_Game()