def Dad_Jokes():
    import requests
    import pyfiglet
    from random import choice
    import termcolor

    header = pyfiglet.figlet_format("DAD JOKES 3000!")
    header = termcolor.colored(header, color="magenta", attrs=["blink"])
    print(header)

    # 
    url = "https://icanhazdadjoke.com/search"
    search = ("y")

    while search[0].lower() == "y":
        term = input("What would you like to search for? ")

        res = requests.get(
            url, 
            headers={"Accept": "application/json"},
            params={"term": term, "limit": 30}
        ).json()

        results = res["results"]
        num_jokes = res["total_jokes"]
        if num_jokes > 1:
            print(f"I found {num_jokes} jokes about {term}. Here is one")
            print("")
            print(choice(results)["joke"])
        elif num_jokes == 1:
            print(f"I found one joke about {term} . Here it is")
            print("")
            print(results[0]["joke"])
        else:
            print(f"Sorry, couldn't find a joke with your term: {term}")
        print("")
        search = input("Would You Like to Search Again?")
    print("Thanks for using us! \U0001f600")

if __name__ == "__main__":
    Dad_Jokes()