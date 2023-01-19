def rt():
    import Data_Retrieval_Att as dt
    import matplotlib.pyplot as plt
    import numpy as np

    x = dt.rt()

    #print(x)

    Date=list(x['Date'])

    English=list(x['English'])

    Math=list(x['Math'])

    Physics=list(x['Physics'])

    Chemistry=list(x['Chemistry'])

    IP=list(x['IP'])

    user_cont = "y"
    user_desout = ""

    print("The available graphs are:\n1.Bar Graph\n2.Line Graph\n3.Pie Chart\n4.Box Plot")
    print()
    print('The entered subjects are\n1. English\n2. Math\n3. Physics\n4. Chemistry\n5. IP')
    print()

    while user_cont[0].lower() == "y":

        user_subno = input("Enter the number of subjects you want to analyse: ")
        
        if user_subno == "":
            print("Please enter some data")
            continue
        if user_subno[0:3].lower() == "one" or user_subno[0] == "1":
            user_desout_1 = "error"
            
            while user_desout_1 == "error":
                user_desout_1 = input("Enter your first subject: ")

                if user_desout_1 == "":
                    print("Please enter some data")
                    user_desout_1 = "error"
                    continue
            
                if user_desout_1[0].lower() == "e" or user_desout_1[0] == "1":
                    user_desout_1 = English
                    sub1="English"
                elif user_desout_1[0].lower() == "m" or user_desout_1[0] == "2":
                    user_desout_1 = Math
                    sub1="Math"
                elif user_desout_1[0].lower() == "p" or user_desout_1[0] == "3":
                    user_desout_1 = Physics
                    sub1="Physics"
                elif user_desout_1[0].lower() == "c" or user_desout_1[0] == "4":
                    user_desout_1 = Chemistry
                    sub1="Chemistry"
                elif user_desout_1[0].lower() == "i" or user_desout_1[0] == "5":
                    user_desout_1 = IP
                    sub1="IP"
                else:
                    print("Enter a valid first subject!")
                    user_desout_1 = "error"
                    continue

            user_desout = input("Which graph would you like to use: \n")
            if user_desout == "":
                print("Please enter some data")
                continue
            if user_desout[0:3].lower() == "bar" or user_desout[0] == "1":
                X_axis = np.arange(len(Date))
                plt.bar(X_axis +.2,user_desout_1, color='lime')

                plt.xticks(X_axis, Date)
                plt.title(f"{sub1} Data Analysis") 
                plt.xlabel("Day") 
                plt.ylabel("Attendance ") 
                plt.grid(True)
                plt.legend([sub1], loc='upper left',fancybox=True, framealpha=1, shadow=True, borderpad=1)
                plt.show()
                user_cont = input("Would you like to search again?")
                if user_cont == "":
                    user_cont = "y"
                user_desout_1 = "error"
                user_subno = None
                continue
                
            elif user_desout[0:4].lower() == "line" or user_desout[0] == "2":
                plt.plot(Date, user_desout_1)
                plt.xticks(Date)
                plt.ylim(0, max(user_desout_1) + 1)
                plt.title(f"{sub1} Data Analysis")
                plt.xlabel("Day") 
                plt.ylabel("Attendance ")
                plt.grid(True)
                plt.legend([sub1], loc='upper left',fancybox=True, framealpha=1, shadow=True, borderpad=1)
                plt.show()
                user_cont = input("Would you like to analyse attendance again?")
                if user_cont == "":
                    user_cont = "y"
                user_desout_1 = "error"
                user_subno = None
                continue
            
            
            elif user_desout[0:3].lower() == "pie" or user_desout[0] == "3":
                plt.pie(user_desout_1, labels=Date)
                plt.title(f"{sub1} Data Analysis")
                plt.show()
                user_cont = input("Would you like to analyse attendance again?")
                if user_cont == "":
                    user_cont = "y"
                user_desout_1 = "error"
                user_subno = None
                continue 
                                
            elif user_desout[0:3].lower() == "box" or user_desout[0] == "4":
                data=[user_desout_1]
                plt.boxplot(data, vert=1, labels=[sub1], showmeans=True)
                plt.title(f"{sub1} Data Analysis")
                plt.show()
                user_cont = input("Would you like to analyse attendance again?")
                if user_cont == "":
                    user_cont = "y"
                user_desout_1 = "error"
                user_subno = None
                continue

        
        
        
        elif user_subno[0:3].lower() == "two" or user_subno[0] == "2":
            user_desout_1 = "error"
            user_desout_2 = "error"
            
            
            while user_desout_1 == "error" or user_desout_2 == "error":
                user_desout_1 = input("Enter your first subject: ")
                user_desout_2 = input("Enter the second subject: ")

                if user_desout_1 == "":
                    print("Please enter some data")
                    user_desout_1 = "error"
                    continue

                if user_desout_2 == "":
                    print("Please enter some data")
                    user_desout_2 = "error"
                    continue
                    
                if user_desout_1[0].lower() == "e" or user_desout_1[0] == "1":
                    user_desout_1 = English
                    sub1="English"
                elif user_desout_1[0].lower() == "m" or user_desout_1[0] == "2":
                    user_desout_1 = Math
                    sub1="Math"
                elif user_desout_1[0].lower() == "p" or user_desout_1[0] == "3":
                    user_desout_1 = Physics
                    sub1="Physics"
                elif user_desout_1[0].lower() == "c" or user_desout_1[0] == "4":
                    user_desout_1 = Chemistry
                    sub1="Chemistry"
                elif user_desout_1[0].lower() == "i" or user_desout_1[0] == "5":
                    user_desout_1 = IP
                    sub1="IP"
                else:
                    print("Enter a valid first subject!")
                    user_desout_1 = "error"
                    continue
                    
                if user_desout_2[0].lower() == "e" or user_desout_2[0] == "1":
                    user_desout_2 = English
                    sub2="English"
                elif user_desout_2[0].lower() == "m" or user_desout_2[0] == "2":
                    user_desout_2 = Math
                    sub2="Math"
                elif user_desout_2[0].lower() == "p" or user_desout_2[0] == "3":
                    user_desout_2 = Physics
                    sub2="Physics"
                elif user_desout_2[0].lower() == "c" or user_desout_2[0] == "4":
                    user_desout_2 = Chemistry
                    sub2="Chemistry"
                elif user_desout_2[0].lower() == "i" or user_desout_2[0] == "5":
                    user_desout_2 = IP
                    sub2="IP"
                else:
                    print("Enter a valid second subject!")
                    user_desout_2 = "error"
                    continue
                                
            user_desout = input("Which graph would you like to use: \n")
            if user_desout == "":
                print("Please enter some data")
                continue
            if user_desout[0:3].lower() == "bar" or user_desout[0] == "1":
                X_axis = np.arange(len(Date))
                plt.bar(X_axis +.2,user_desout_1,width= 0.4, color='lime')
                plt.bar(X_axis -.2 ,user_desout_2,width= 0.4, color='magenta')
                plt.xticks(X_axis, Date)
                plt.title(f"{sub1} vs {sub2} Comparison") 
                plt.xlabel("Day") 
                plt.ylabel("Attendance ") 
                plt.grid(True)
                plt.legend([sub1, sub2], loc='upper left',fancybox=True, framealpha=1, shadow=True, borderpad=1)
                plt.show()
                user_cont = input("Would you like to analyse attendance again?")
                if user_cont == "":
                    user_cont = "y"
                user_desout_1 = "error"
                user_desout_2 = "error"
                user_subno = None
                continue
                
                

            elif user_desout[0:4].lower() == "line" or user_desout[0] == "2":
                plt.plot(Date, user_desout_1)
                plt.plot(Date, user_desout_2)
                plt.xticks(Date)
                plt.title(f"{sub1} vs {sub2} Comparison")
                plt.xlabel("Day") 
                plt.ylabel("Attendance ")
                plt.grid(True)
                plt.legend([sub1, sub2], loc='upper left',fancybox=True, framealpha=1, shadow=True, borderpad=1)
                plt.show()
                user_cont = input("Would you like to analyse attendance again?")
                if user_cont == "":
                    user_cont = "y"
                user_desout_1 = "error"
                user_desout_2 = "error"
                user_subno = None
                continue
            
            elif user_desout[0:3].lower() == "pie" or user_desout[0] == "3":
                user_sub_sum_1 = 0
                user_sub_sum_2 = 0
                for char in user_desout_1:
                    user_sub_sum_1 += char
                for char in user_desout_2:
                    user_sub_sum_2 += char

                if user_sub_sum_1 > user_sub_sum_2:
                    myexplode = [0.2, 0]
                elif user_sub_sum_2 > user_sub_sum_1:
                    myexplode = [0, 0.2]
                else:
                    myexplode = [0.1, 0.1]
                

                pie_subj = [sub1, sub2]
                data = [user_sub_sum_1, user_sub_sum_2]
                plt.pie(data, labels=pie_subj, explode=myexplode, autopct="%1.2f%%")
                plt.title(f"{sub1} vs {sub2} Comparison")
                plt.show()
                user_cont = input("Would you like to analyse attendance again?")
                if user_cont == "":
                    user_cont = "y"
                user_desout_1 = "error"
                user_desout_2 = "error"
                continue
                
            elif user_desout[0:3].lower() == "box" or user_desout[0] == "4":
                data=[user_desout_1, user_desout_2]
                plt.boxplot(data, vert=1, labels=[sub1,sub2], showmeans=True)
                plt.title(f"{sub1} vs {sub2} Comparison")
                plt.show()
                user_cont = input("Would you like to analyse attendance again?")
                if user_cont == "":
                    user_cont = "y"
                user_desout_1 = "error"
                user_desout_2 = "error"
                user_subno = None
                continue

        
        elif user_subno[0:5].lower() == "three" or user_subno[0] == "3":

        
            user_desout_1 = "error"
            user_desout_2 = "error"
            user_desout_3 = "error"


            
            
            while user_desout_1 == "error" or user_desout_2 == "error" or user_desout_3 == "error":
                user_desout_1 = input("Enter your first subject: ")
                user_desout_2 = input("Enter the second subject: ")
                user_desout_3 = input("Enter the third subject: ")
                if user_desout_1 == "":
                    print("Please enter some data")
                    user_desout_1 = "error"
                    continue    
                if user_desout_2 == "":
                    print("Please enter some data")
                    user_desout_2 = "error"
                    continue    
                if user_desout_3 == "":
                    print("Please enter some data")
                    user_desout_3 = "error"
                    continue
                
                if user_desout_1[0].lower() == "e" or user_desout_1[0] == "1":
                    user_desout_1 = English
                    sub1="English"
                elif user_desout_1[0].lower() == "m" or user_desout_1[0] == "2":
                    user_desout_1 = Math
                    sub1="Math"
                elif user_desout_1[0].lower() == "p" or user_desout_1[0] == "3":
                    user_desout_1 = Physics
                    sub1="Physics"
                elif user_desout_1[0].lower() == "c" or user_desout_1[0] == "4":
                    user_desout_1 = Chemistry
                    sub1="Chemistry"
                elif user_desout_1[0].lower() == "i" or user_desout_1[0] == "5":
                    user_desout_1 = IP
                    sub1="IP"
                else:
                    print("Enter a valid first subject!")
                    user_subno = None
                    user_desout_1 = "error"
                    user_desout_2 = "error"
                    user_desout_3 = "error"
                    continue
                    
                if user_desout_2[0].lower() == "e" or user_desout_2[0] == "1":
                    user_desout_2 = English
                    sub2="English"
                elif user_desout_2[0].lower() == "m" or user_desout_2[0] == "2":
                    user_desout_2 = Math
                    sub2="Math"
                elif user_desout_2[0].lower() == "p" or user_desout_2[0] == "3":
                    user_desout_2 = Physics
                    sub2="Physics"
                elif user_desout_2[0].lower() == "c" or user_desout_2[0] == "4":
                    user_desout_2 = Chemistry
                    sub2="Chemistry"
                elif user_desout_2[0].lower() == "i" or user_desout_2[0] == "5":
                    user_desout_2 = IP
                    sub2="IP"
                else:
                    print("Enter a valid second subject!")
                    user_subno = None
                    user_desout_1 = "error"
                    user_desout_2 = "error"
                    user_desout_3 = "error"
                    continue

                if user_desout_3[0].lower() == "e" or user_desout_3[0] == "1":
                    user_desout_3 = English
                    sub3="English"
                elif user_desout_3[0].lower() == "m" or user_desout_3[0] == "2":
                    user_desout_3 = Math
                    sub3="Math"
                elif user_desout_3[0].lower() == "p" or user_desout_3[0] == "3":
                    user_desout_3 = Physics
                    sub3="Physics"
                elif user_desout_3[0].lower() == "c" or user_desout_3[0] == "4":
                    user_desout_3 = Chemistry
                    sub3="Chemistry"
                elif user_desout_3[0].lower() == "i" or user_desout_3[0] == "5":
                    user_desout_3 = IP
                    sub3="IP"
                else:
                    print("Enter a valid third subject!")
                    user_subno = None
                    user_desout_1 = "error"
                    user_desout_2 = "error"
                    user_desout_3 = "error"
                    continue

            user_desout = input("Which graph would you like to use: \n")
            if user_desout == "":
                print("Please enter some data")
                continue
            if user_desout[0:3].lower() == "bar" or user_desout[0] == "1":
                X_axis = np.arange(len(Date))
                plt.bar(X_axis +.3,user_desout_1,width= 0.3, color='lime')
                plt.bar(X_axis ,user_desout_2,width= 0.3, color='magenta')
                plt.bar(X_axis -.3, user_desout_3, width = 0.3, color='blue')
                plt.xticks(X_axis, Date)
                plt.title(f"{sub1} vs {sub2} vs {sub3} Comparison") 
                plt.xlabel("Day") 
                plt.ylabel("Attendance ") 
                plt.grid(True)
                plt.legend([sub1, sub2, sub3], loc='upper left',fancybox=True, framealpha=1, shadow=True, borderpad=1)
                plt.show()
                user_cont = input("Would you like to analyse attendance again?")
                if user_cont == "":
                    user_cont = "y"
                user_desout_1 = "error"
                user_desout_2 = "error"
                user_desout_3 = "error"
                user_subno = None
                continue

            elif user_desout[0:4].lower() == "line" or user_desout[0] == "2":
                plt.plot(Date, user_desout_1)
                plt.plot(Date, user_desout_2)
                plt.plot(Date, user_desout_3)
                plt.xticks(Date)
                plt.title(f"{sub1} vs {sub2} vs {sub3} Comparison")
                plt.xlabel("Day") 
                plt.ylabel("Attendance ")
                plt.grid(True)
                plt.legend([sub1, sub2, sub3], loc='upper left',fancybox=True, framealpha=1, shadow=True, borderpad=1)
                plt.show()
                user_cont = input("Would you like to analyse attendance again?")
                if user_cont == "":
                    user_cont = "y"
                user_desout_1 = "error"
                user_desout_2 = "error"
                user_desout_3 = "error"
                user_subno = None
                continue
            
            elif user_desout[0:3].lower() == "pie" or user_desout[0] == "3":
                user_sub_sum_1 = 0
                user_sub_sum_2 = 0
                user_sub_sum_3 = 0
                for char in user_desout_1:
                    user_sub_sum_1 += char
                for char in user_desout_2:
                    user_sub_sum_2 += char
                for char in user_desout_3:
                    user_sub_sum_3 += char

                if user_sub_sum_1 > user_sub_sum_2 and user_sub_sum_1 > user_sub_sum_3:
                    myexplode = [0.2, 0, 0]
                elif user_sub_sum_2 > user_sub_sum_1 and user_sub_sum_2 > user_sub_sum_3:
                    myexplode = [0, 0.2, 0]
                elif user_sub_sum_3 > user_sub_sum_1 and user_sub_sum_3 > user_sub_sum_2:
                    myexplode=[0, 0, 0.2]
                else:
                    myexplode = [0.1, 0.1, 0.1]

                pie_subj = [sub1, sub2, sub3]
                data = [user_sub_sum_1, user_sub_sum_2, user_sub_sum_3]
                
                plt.pie(data, labels=pie_subj, explode= myexplode, autopct="%1.2f%%")
                plt.title(f"{sub1} vs {sub2} vs {sub3} Comparison")
                plt.show()
                user_cont = input("Would you like to analyse attendance again?")
                if user_cont == "":
                    user_cont = "y"
                user_desout_1 = "error"
                user_desout_2 = "error"
                user_desout_3 = "error"
                user_subno = None
                continue
                
            elif user_desout[0:3].lower() == "box" or user_desout[0] == "4":
                data=[user_desout_1, user_desout_2, user_desout_3]
                plt.boxplot(data, vert=1, labels=[sub1,sub2, sub3], showmeans=True)
                plt.title(f"{sub1} vs {sub2} vs {sub3} Comparison")
                plt.show()
                user_cont = input("Would you like to analyse attendance again?")
                if user_cont == "":
                    user_cont = "y"
                user_desout_1 = "error"
                user_desout_2 = "error"
                user_desout_3 = "error"
                user_subno = None
                continue

        
        

        elif user_subno[0:4].lower() == "four" or user_subno[0] == "4":

        
            user_desout_1 = "error"
            user_desout_2 = "error"
            user_desout_3 = "error"
            user_desout_4 = "error"
            
            
            while user_desout_1 == "error" or user_desout_2 == "error" or user_desout_3 == "error" or user_desout_4 == "error":
                user_desout_1 = input("Enter your first subject: ")
                user_desout_2 = input("Enter the second subject: ")
                user_desout_3 = input("Enter the third subject: ")
                user_desout_4 = input("Enter the fourth subject:  ")

                if user_desout_1 == "":
                    print("Please enter some data")
                    user_desout_1 = "error"
                    continue
                if user_desout_2 == "":
                    print("Please enter some data")
                    user_desout_2 = "error"
                    continue    
                if user_desout_3 == "":
                    print("Please enter some data")
                    user_desout_3 = "error"
                    continue
                if user_desout_4 == "":
                    print("Please enter some data")
                    user_desout_4 = "error"
                    continue


                if user_desout_1[0].lower() == "e" or user_desout_1[0] == "1":
                    user_desout_1 = English
                    sub1="English"
                elif user_desout_1[0].lower() == "m" or user_desout_1[0] == "2":
                    user_desout_1 = Math
                    sub1="Math"
                elif user_desout_1[0].lower() == "p" or user_desout_1[0] == "3":
                    user_desout_1 = Physics
                    sub1="Physics"
                elif user_desout_1[0].lower() == "c" or user_desout_1[0] == "4":
                    user_desout_1 = Chemistry
                    sub1="Chemistry"
                elif user_desout_1[0].lower() == "i" or user_desout_1[0] == "5":
                    user_desout_1 = IP
                    sub1="IP"
                else:
                    print("Enter a valid first subject!")
                    user_subno = None
                    user_desout_1 = "error"
                    user_desout_2 = "error"
                    user_desout_3 = "error"
                    user_desout_4 = "error"
                    continue
                    
                if user_desout_2[0].lower() == "e" or user_desout_2[0] == "1":
                    user_desout_2 = English
                    sub2="English"
                elif user_desout_2[0].lower() == "m" or user_desout_2[0] == "2":
                    user_desout_2 = Math
                    sub2="Math"
                elif user_desout_2[0].lower() == "p" or user_desout_2[0] == "3":
                    user_desout_2 = Physics
                    sub2="Physics"
                elif user_desout_2[0].lower() == "c" or user_desout_2[0] == "4":
                    user_desout_2 = Chemistry
                    sub2="Chemistry"
                elif user_desout_2[0].lower() == "i" or user_desout_2[0] == "5":
                    user_desout_2 = IP
                    sub2="IP"
                else:
                    print("Enter a valid second subject!")
                    user_subno = None
                    user_desout_1 = "error"
                    user_desout_2 = "error"
                    user_desout_3 = "error"
                    user_desout_4 = "error"
                    continue

                if user_desout_3[0].lower() == "e" or user_desout_3[0] == "1":
                    user_desout_3 = English
                    sub3="English"
                elif user_desout_3[0].lower() == "m" or user_desout_3[0] == "2":
                    user_desout_3 = Math
                    sub3="Math"
                elif user_desout_3[0].lower() == "p" or user_desout_3[0] == "3":
                    user_desout_3 = Physics
                    sub3="Physics"
                elif user_desout_3[0].lower() == "c" or user_desout_3[0] == "4":
                    user_desout_3 = Chemistry
                    sub3="Chemistry"
                elif user_desout_3[0].lower() == "i" or user_desout_3[0] == "5":
                    user_desout_3 = IP
                    sub3="IP"
                else:
                    print("Enter a valid third subject!")
                    user_subno = None
                    user_desout_1 = "error"
                    user_desout_2 = "error"
                    user_desout_3 = "error"
                    user_desout_4 = "error"
                    continue

                if user_desout_4[0].lower() == "e" or user_desout_4[0] == "1":
                    user_desout_4 = English
                    sub4="English"
                elif user_desout_4[0].lower() == "m" or user_desout_4[0] == "2":
                    user_desout_4 = Math
                    sub4="Math"
                elif user_desout_4[0].lower() == "p" or user_desout_4[0] == "3":
                    user_desout_4 = Physics
                    sub4="Physics"
                elif user_desout_4[0].lower() == "c" or user_desout_4[0] == "4":
                    user_desout_4 = Chemistry
                    sub4="Chemistry"
                elif user_desout_4[0].lower() == "i" or user_desout_4[0] == "5":
                    user_desout_4 = IP
                    sub4="IP"
                else:
                    print("Enter a valid first subject!")
                    user_subno = None
                    user_desout_1 = "error"
                    user_desout_2 = "error"
                    user_desout_3 = "error"
                    user_desout_4 = "error"
                    continue

            user_desout = input("Which graph would you like to use: \n")
            if user_desout == "":
                print("Please enter some data")
                continue
            if user_desout[0:3].lower() == "bar" or user_desout[0] == "1":
                X_axis = np.arange(len(Date))
                plt.bar(X_axis +.2,user_desout_1,width= 0.2, color='lime')
                plt.bar(X_axis ,user_desout_2,width= 0.2, color='magenta')
                plt.bar(X_axis -.2,user_desout_3,width= 0.2, color='orange')
                plt.bar(X_axis -.4, user_desout_4, width = 0.2, color='blue')
                plt.xticks(X_axis, Date)
                plt.title(f"{sub1} vs {sub2} vs {sub3} vs {sub4} Comparison") 
                plt.xlabel("Day") 
                plt.ylabel("Attendance ") 
                plt.grid(True)
                plt.legend([sub1, sub2, sub3, sub4], loc='upper left',fancybox=True, framealpha=1, shadow=True, borderpad=1)
                plt.show()
                user_cont = input("Would you like to analyse attendance again?")
                if user_cont == "":
                    user_cont = "y"
                user_desout_1 = "error"
                user_desout_2 = "error"
                user_desout_3 = "error"
                user_desout_4 = "error"
                user_subno = None
                continue

            elif user_desout[0:4].lower() == "line" or user_desout[0] == "2":
                plt.plot(Date, user_desout_1)
                plt.plot(Date, user_desout_2)
                plt.plot(Date, user_desout_3)
                plt.plot(Date, user_desout_4)
                plt.xticks(Date)
                plt.title(f"{sub1} vs {sub2} vs {sub3} vs {sub4} Comparison")
                plt.xlabel("Day") 
                plt.ylabel("Attendance ")
                plt.grid(True)
                plt.legend([sub1, sub2, sub3, sub4], loc='upper left',fancybox=True, framealpha=1, shadow=True, borderpad=1)
                plt.show()
                user_cont = input("Would you like to analyse attendance again?")
                if user_cont == "":
                    user_cont = "y"
                user_desout_1 = "error"
                user_desout_2 = "error"
                user_desout_3 = "error"
                user_desout_4 = "error"
                user_subno = None
                continue
            
            elif user_desout[0:3].lower() == "pie" or user_desout[0] == "3":
                user_sub_sum_1 = 0
                user_sub_sum_2 = 0
                user_sub_sum_3 = 0
                user_sub_sum_4 = 0
                for char in user_desout_1:
                    user_sub_sum_1 += char
                for char in user_desout_2:
                    user_sub_sum_2 += char
                for char in user_desout_3:
                    user_sub_sum_3 += char
                for char in user_desout_4:
                    user_sub_sum_4 += char

                if user_sub_sum_1 > user_sub_sum_2 and user_sub_sum_1 > user_sub_sum_3 and user_sub_sum_1 > user_sub_sum_4:
                    myexplode = [0.2, 0, 0, 0]
                elif user_sub_sum_2 > user_sub_sum_1 and user_sub_sum_2 > user_sub_sum_3 and user_sub_sum_2 > user_sub_sum_4:
                    myexplode = [0, 0.2, 0, 0]
                elif user_sub_sum_3 > user_sub_sum_1 and user_sub_sum_3 > user_sub_sum_2 and user_sub_sum_3 > user_sub_sum_4:
                    myexplode=[0, 0, 0.2, 0]
                elif user_sub_sum_4 > user_sub_sum_1 and user_sub_sum_4 > user_sub_sum_2 and user_sub_sum_4 > user_sub_sum_3:
                    myexplode = [0, 0, 0, 0.2]
                else:
                    myexplode = [0.1, 0.1, 0.1, 0.1]

                pie_subj = [sub1, sub2, sub3, sub4]
                data = [user_sub_sum_1, user_sub_sum_2, user_sub_sum_3, user_sub_sum_4]
                
                plt.pie(data, labels=pie_subj, explode= myexplode, autopct="%1.2f%%")
                plt.title(f"{sub1} vs {sub2} vs {sub3} vs {sub4} Comparison")
                plt.show()
                user_cont = input("Would you like to analyse attendance again?")
                if user_cont == "":
                    user_cont = "y"
                user_desout_1 = "error"
                user_desout_2 = "error"
                user_desout_3 = "error"
                user_desout_4 = "error"
                user_subno = None
                continue
                
            elif user_desout[0:3].lower() == "box" or user_desout[0] == "4":
                data=[user_desout_1, user_desout_2, user_desout_3, user_desout_4]
                plt.boxplot(data, vert=1, labels=[sub1,sub2,sub3, sub4], showmeans=True)
                plt.title(f"{sub1} vs {sub2} vs {sub3} vs {sub4} Comparison")
                plt.show()
                user_cont = input("Would you like to analyse attendance again?")
                if user_cont == "":
                    user_cont = "y"
                user_desout_1 = "error"
                user_desout_2 = "error"
                user_desout_3 = "error"
                user_desout_4 = "error"
                user_subno = None
                continue


        elif user_subno[0:4].lower() == "five" or user_subno[0] == "5":
            user_desout_1, user_desout_2, user_desout_3, user_desout_4, user_desout_5 = English, Math, Physics, Chemistry, IP


            sub1, sub2, sub3, sub4, sub5 = "English", "Math", "Physics", "Chemistry", "IP"
            
            
            user_desout = input("Which graph would you like to use: \n")
            if user_desout == "":
                print("Please enter some data")
                continue
            if user_desout[0:3].lower() == "bar" or user_desout[0] == "1":
                X_axis = np.arange(len(Date))
                plt.bar(X_axis +.3,user_desout_1,width= 0.15, color='lime')
                plt.bar(X_axis +.15,user_desout_2,width= 0.15, color='magenta')
                plt.bar(X_axis ,user_desout_3,width= 0.15, color='orange')
                plt.bar(X_axis -.15, user_desout_4, width = 0.15, color='blue')
                plt.bar(X_axis -.3, user_desout_5, width = 0.15, color="yellow")
                plt.xticks(X_axis, Date)
                plt.title(f"{sub1} vs {sub2} vs {sub3} vs {sub4} vs {sub5}Comparison") 
                plt.xlabel("Day") 
                plt.ylabel("Attendance ") 
                plt.grid(True)
                plt.legend([sub1, sub2, sub3, sub4, sub5], loc='upper left',fancybox=True, framealpha=1, shadow=True, borderpad=1)
                plt.show()
                user_cont = input("Would you like to analyse attendance again?")
                if user_cont == "":
                    user_cont = "y"
                user_desout_1 = "error"
                user_desout_2 = "error"
                user_desout_3 = "error"
                user_desout_4 = "error"
                user_desout_5 = "error"
                user_subno = None
                continue

            elif user_desout[0:4].lower() == "line" or user_desout[0] == "2":
                plt.plot(Date, user_desout_1)
                plt.plot(Date, user_desout_2)
                plt.plot(Date, user_desout_3)
                plt.plot(Date, user_desout_4)
                plt.plot(Date, user_desout_5)
                plt.xticks(Date)
                plt.title(f"{sub1} vs {sub2} vs {sub3} vs {sub4} vs {sub5} Comparison")
                plt.xlabel("Day") 
                plt.ylabel("Attendance ")
                plt.grid(True)
                plt.legend([sub1, sub2, sub3, sub4, sub5], loc='upper left',fancybox=True, framealpha=1, shadow=True, borderpad=1)
                plt.show()
                user_cont = input("Would you like to analyse attendance again?")
                if user_cont == "":
                    user_cont = "y"
                user_desout_1 = "error"
                user_desout_2 = "error"
                user_desout_3 = "error"
                user_desout_4 = "error"
                user_desout_5 = "error"
                user_subno = None
                continue
            
            elif user_desout[0:3].lower() == "pie" or user_desout[0] == "3":
                user_sub_sum_1 = 0
                user_sub_sum_2 = 0
                user_sub_sum_3 = 0
                user_sub_sum_4 = 0
                user_sub_sum_5 = 0
                for char in user_desout_1:
                    user_sub_sum_1 += char
                for char in user_desout_2:
                    user_sub_sum_2 += char
                for char in user_desout_3:
                    user_sub_sum_3 += char
                for char in user_desout_4:
                    user_sub_sum_4 += char
                for char in user_desout_5:
                    user_sub_sum_5 += char

                if user_sub_sum_1 > user_sub_sum_2 and user_sub_sum_1 > user_sub_sum_3 and user_sub_sum_1 > user_sub_sum_4 and user_desout_5 :
                    myexplode = [0.2, 0, 0, 0, 0]
                elif user_sub_sum_2 > user_sub_sum_1 and user_sub_sum_2 > user_sub_sum_3 and user_sub_sum_2 > user_sub_sum_4 and user_desout_5:
                    myexplode = [0, 0.2, 0, 0, 0]
                elif user_sub_sum_3 > user_sub_sum_1 and user_sub_sum_3 > user_sub_sum_2 and user_sub_sum_3 > user_sub_sum_4 and user_desout_5:
                    myexplode=[0, 0, 0.2, 0, 0]
                elif user_sub_sum_4 > user_sub_sum_1 and user_sub_sum_4 > user_sub_sum_2 and user_sub_sum_4 > user_sub_sum_3 and user_desout_5:
                    myexplode = [0, 0, 0, 0.2, 0]
                elif user_desout_5 > user_desout_1 and user_desout_5 > user_desout_2 and user_desout_5 > user_desout_3 and user_desout_5 > user_desout_4:
                    myexplode = [0, 0, 0, 0, 0.2]
                else:
                    myexplode = [0.1, 0.1, 0.1, 0.1, 0.1]

                pie_subj = [sub1, sub2, sub3, sub4, sub5]
                data = [user_sub_sum_1, user_sub_sum_2, user_sub_sum_3, user_sub_sum_4, user_sub_sum_5]
                
                plt.pie(data, labels=pie_subj, explode= myexplode, autopct="%1.2f%%")
                plt.title(f"{sub1} vs {sub2} vs {sub3} vs {sub4} vs {sub5} Comparison")
                plt.show()
                user_cont = input("Would you like to analyse attendance again?")
                if user_cont == "":
                    user_cont = "y"
                user_desout_1 = "error"
                user_desout_2 = "error"
                user_desout_3 = "error"
                user_desout_4 = "error"
                user_desout_5 = "error"
                user_subno = None
                continue
                
            elif user_desout[0:3].lower() == "box" or user_desout[0] == "4":
                data=[user_desout_1, user_desout_2, user_desout_3, user_desout_4, user_desout_5]
                plt.boxplot(data, vert=1, labels=[sub1,sub2,sub3, sub4, sub5], showmeans=True)
                plt.title(f"{sub1} vs {sub2} vs {sub3} vs {sub4} vs {sub5} Comparison")
                plt.show()
                user_cont = input("Would you like to analyse attendance again?")
                if user_cont == "":
                    user_cont = "y"
                user_desout_1 = "error"
                user_desout_2 = "error"
                user_desout_3 = "error"
                user_desout_4 = "error"
                user_desout_5 = "error"
                user_subno = None
                continue


    print("Thank you")
            
if __name__ == "__main__":
    rt()