def rt():
    import Data_Retrieval_Tea as dt
    import matplotlib.pyplot as plt
    import numpy as np
    import termcolor

    x = dt.rt()

    #print(x)


    Date=list(x['Date'])

    English=list(x['English'])

    Math=list(x['Math'])

    Physics=list(x['Physics'])

    Chemistry=list(x['Chemistry'])

    IP=list(x['IP'])
    
    English_Absent, English_Present = 0,0
    Math_Absent, Math_Present = 0,0
    Physics_Absent, Physics_Present = 0,0
    Chemistry_Absent, Chemistry_Present = 0,0
    IP_Absent, IP_Present = 0,0
    
    
    for char in English:
        if char == "A":
            English_Absent += 1
   
        else:
            English_Present += 1
    
         
    for char in Math:
        if char == "A":
            Math_Absent += 1
        else:
            Math_Present += 1
            
    for char in Physics:
        if char == "A":
            Physics_Absent += 1
        else:
            Physics_Present += 1
            
    for char in Chemistry:
        if char == "A":
            Chemistry_Absent += 1
        else:
            Chemistry_Present += 1
            
    for char in IP:
        if char == "A":
            IP_Absent += 1
        else:
            IP_Present += 1
    

    Total_Present = [English_Present, Math_Present, Physics_Present, Chemistry_Present, IP_Present]
    Total_Absent = [English_Absent, Math_Absent, Physics_Absent, Chemistry_Absent, IP_Absent]
    y = English_Present + English_Absent
    Total_Days = range(1, y+1)
    
    print("The available graphs are:\n1.Bar Graph\n2.Line Graph\n3.Table")
    user_cont = "y"
    user_desout = ""
    X_Axis = ['English', 'Physics', 'Chemistry', 'Maths', 'IP']
    while user_cont[0].lower() == "y":
        user_desout = input("What kind of graph would you like to use? ")
        if user_desout == "":
            print("Please enter some data")
        elif user_desout[0] == "1" or user_desout[0:3].lower() == "bar":
            plt.bar(X_Axis, Total_Present)
            plt.bar(X_Axis, Total_Absent , width=0.3)
            plt.xlabel("Subject Teacher")
            plt.ylabel("Total number of working days")
            plt.title("Teacher Attendance")
            plt.yticks(Total_Days)
            plt.legend(["Number of days present", "Number of days absent"], loc="upper left")
            plt.show()
            user_cont = input("Would you like to search again?")
        elif user_desout[0] == "2" or user_desout[0:4].lower() == "line":
            plt.plot(X_Axis, Total_Present)
            plt.xlabel("Subject Teacher")
            plt.ylabel("Total number of working days")
            plt.yticks(Total_Days)
            plt.title("Teacher's Presentee Data")
            plt.plot(X_Axis, Total_Absent, linestyle="dotted", color="red")
            plt.legend("Total Present", "Total Absent")
            plt.show()
            user_cont = input("Would you like to search again?")
        elif user_desout[0] == "3" or user_desout[0:3].lower() == "att":
            print(x)
            user_cont = input("Would you like to search again?")


                        


            
if __name__ == "__main__":
    rt()