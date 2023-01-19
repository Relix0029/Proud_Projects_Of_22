import Data_Introduction_V2 as ent
import Data_Representation_Cla as drc
import Data_Representation_Att as dra
import Data_Representation_Tea as drt
import pymysql 

user_cont = "y"

while user_cont[0].lower() == "y":
    user_input = input("Would you like to \n1. Make a new entry \n2. Analyse previously entered data \n3. Delete all records: \n")
    
    if user_input == "":
        print("Enter some valid input")
        continue
    
    if user_input[0] == "1" or user_input[0:5].lower() == "entry":
        userint = input("What dataset would you like to add to?\n (1. Attendance / 2. Classes / 3. Teacher's Attendance)")
        if userint == "1" or userint[0].lower() == "a":
            ent.ent1()
            user_cont = input("Would you like to go again? ")
            continue
        elif userint == "2" or userint[0].lower() == "c":
            ent.ent2()
            user_cont = input("Would you like to go again? ")
            continue
        elif userint == "3" or userint[0].lower() == "t":
            ent.ent3()
            user_cont = input("Would you like to go again? ")
            continue
        else:
            print("Please enter a valid input and try again later")
            user_cont = input("Would you like to go again? ")
            continue
            
            
    
    
    if user_cont == "":
        user_cont = "y"
            
        
        if user_cont[0].lower() == "y":
            continue
        
    elif user_input[0] == "2" or user_input[0:7].lower() == "analyse":
        usint = input("What would you like to analyse? \n (1. Attendance / 2. Classes / 3. Teacher's Attendance')")
        if usint[0] == "1" or usint[0:3].lower() == "att":
            dra.rt()
        elif usint[0] == "2" or usint[0:3].lower() == "cla":
            drc.rt()
        elif usint[0] == "3" or usint[0:3].lower() == "tea":
            drt.rt()
        else:
            print("Please man respect our program")
        user_cont = input("Would you like to go again? ")
        
        if user_cont == "":
            user_cont = "y"
            
        
        if user_cont[0].lower() == "y":
            continue
        
    elif user_input[0] == "3" or user_input[0:6].lower() == "delete":
        connection = pymysql.connect(host='localhost',user='root',password='Admin',db='XII_Project')
        cursor=connection.cursor()
        x = input("Would you like to delete \n 1. Attendance Data \n 2. Classes Data \n 3.Teachers \n 4. All Data ")
        if x[0:3].lower() == "att" or x[0] == "1":
            sql = "delete from attendance"
            cursor.execute(sql)
        elif x[0:3].lower() == "cla" or x[0] == "2":
            sql = "delete from dailystats;"
            cursor.execute(sql)
        elif x[0:3].lower() == "tea" or x[0] == "3":
            sql = "delete from teachers"
            cursor.execute(sql)
        elif x[0:3].lower() == "bot" or x[0:3].lower() == "all" or x[0] == "4":
            sql = "delete from dailystats;"
            cursor.execute(sql)
            sql = "delete from attendance"
            cursor.execute(sql)
            sql = "delete from teachers"
            cursor.execute(sql)
        else:
            print("Please enter a valid input!!")
            continue
        connection.commit()
        user_cont = input("Would you like to go again? ")
        
        if user_cont == "":
            user_cont = "y"
        
        if user_cont[0].lower() == "y":
            continue
        
    else:
        print("Thank you and have a nice day!")