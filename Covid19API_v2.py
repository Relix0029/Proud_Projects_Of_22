def Covid_Run():
    import termcolor
    import pyfiglet
    import requests
    
    msg = pyfiglet.figlet_format("Covid 19 tracking systems")
    msg = termcolor.colored(msg, color="red", attrs=["blink"])
    print(msg)

    Search =("Y")

    while Search[0] == "Y" or Search[0] == "y":
        url = "https://api.covid19india.org/state_district_wise.json"
        res = requests.get(url).json()
        x = input("Would you like to see the list of the states where tracking is availabe?")
        
       
        if x[0] == "y" or x[0] == "Y":
                for key in res: 
                    print (key)
                    print("")  

        term = input("Choose one state for analysis: ")
        term = term.lower()
        term = term.title()

        # Pulling data from API
        run = False
        res = requests.get(
            url,
            headers={"Accept": "application/json"},
            params={"term": term, "limit": 30}
        ).json()

        # Polishing into dict
        while run == False:
            try:
                state = (res[term])
                run = True
            except KeyError as err:
                print(err)
                print("Please check spelling and//or spacing and try again")
                term = input("Which state would you like to search for? ")
                term = term.lower()
                term = term.title()
                

        district = (state["districtData"])

        x = input("Would you like to see a list of districts tracked for the given state? ")
        if x[0] == "y" or x[0] == "Y":
            for key in district: 
                print(key)
                print("") 

        city = input("Which district would you like to search for? ")
        city = city.lower()
        city = city.title()
        run = False
        while run == False:
            try:    
                data = (district[city])
                run = True
            except KeyError as err:
                print(err)
                print("Please check spelling and//or spacing and try again")
                city = input("Which district would you like to search for? ")
                city = city.lower()
                city = city.title()
                continue


            # All of the data about searched term is here
            active = data["active"]
            confirmed = data["confirmed"]
            deceased = data["deceased"]
            recovered = data["recovered"]

            # Printing all data for user to see
            print("")
            print(f"These are the stats for covid 19 in {city}")
            print("")
            print(f"Active Covid Cases = {active}")
            print(f"Confirmed Covid Cases = {confirmed}")
            print(f"Deceased Covid Cases = {deceased}")
            print(f"Recovered Covid Cases = {recovered}")

            # Asking if user wants to search again
            Search = input("Would you like to search again?")
    print("See You Next Time! \U0001f600")
if __name__ == "__main__":
    Covid_Run()


