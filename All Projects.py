import pyfiglet
import termcolor
import time
run = ("y")
x = pyfiglet.figlet_format("Ali Khan Projects")
x = termcolor.colored(x, color="blue", attrs=["blink"])
print(x)
print("Hint: Use Numbers for input of program")

while run[0] == "y" or run[0] == "Y":
    print("What would you like to run?")
    print("1. Covid Tracker")
    print("2. Dad Jokes")
    print("3. Guessing Game")
    print("4. RPS(Rock Paper Scissors)")
    x = input()
    x = x.lower()

    if x == "1" or x == "covid tracker":
        import Covid19API_v2
        print("Getting Covid Tracker...")
        time.sleep(2)
        print("\n"*100)
        Covid19API_v2.Covid_Run()
        print("Closing Covid Tracker...")
        time.sleep(2)
        print("")
        run = input("Would you like to return to the interpreter? ")

    elif x == "2" or x == "dad jokes":
        import Dad
        print("Getting Dad Jokes...")
        time.sleep(2)
        Dad.Dad_Jokes()
        print("Closing Dad Jokes")
        time.sleep(2)
        run = input("Would you like to return to the interpreter? ")

    elif x == "3" or x == "guessing game":
        import Guessing_Game_v2
        print("Getting Guessing Game...")
        time.sleep(2)
        Guessing_Game_v2.Play_Game()
        print("Closing Guessing Game...")
        time.sleep(2)
        run = input("Would you like to return to the interpreter? ")

    elif x == "4" or x == "rps" or x == "rock paper scissors":
        import RPS_v2
        print("Getting Rock Paper Scissors...")
        time.sleep(2)
        RPS_v2.Play_Game()
        print("Closing RPS Game...")
        time.sleep(2)
        run = input("Would you like to return to the interpreter? ")

    else:
        print("Sorry, invalid input.\nPlease try again")

print("Visit again later! \U0001f600")