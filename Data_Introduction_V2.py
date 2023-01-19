def ent1():
    import pymysql

    connection = pymysql.connect(host='localhost',user='root',password='Admin',db='XII_Project')
    cursor = connection.cursor()

    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    err = ["00","32","33","34","35","36","37","38","39"]
    Day = input("Enter the Date (DD):  ")
    
    while len(Day) != 2:
        print("Please check the given format and try again")
        Day = input("Enter the Date (DD):  ")
    
    x = False
    while x == False:
        if Day[0] not in numbers[0:4]:
            print("The supplied value is not a valid date. Please try again")    
            Day = input("Enter the Date (DD):  ")
            
        
        elif Day[1] not in numbers:
            print("The supplied value is not a valid date. Please try again")    
            Day = input("Enter the Date (DD):  ")
            
        
        elif Day in err:
            print("The supplied value is not a valid date. Please try again")
            Day = input("Enter the Date (DD): ") 
            
        else:
            x = True
        
    Day = str(Day)
 
    Months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    Month = input("Enter the Month (MM):  ")
    x = False
    while x == False:

        while Month not in Months:
            print("The supplied value is not a valid month. Please try again")    
            Month = input("Enter the Month (MM):  ")
            
        if Month in Months:
            x = True
        


    Year = input("Enter the Year (YYYY):  ")
    while type(Year) != int:
        try:
            Year = int(Year)
        except:
            print("The supplied value is not a number. Please try again")    
            Year = input("Enter the Year (YYYY):  ")
    Year = str(Year)

    _Date_ = Year + "-" + Month + "-" + Day
    print(_Date_)
    
    English = input("Enter the attendance for English:")
    while type(English) != int:
        try:
            English = int(English)
        except:
            print("The supplied value is not a number. Please try again")
            English = input("Enter the attendance for English:")
            
    Math = input("Enter the attendance for Math: ")
    while type(Math) != int:
        try:
            Math = int(Math)
        except:
            print("The supplied value is not a number. Please try again")
            Math = input("Enter the attendance for Math: ")
            
    Physics = input("Enter the attendance for Physics: ")
    while type(Physics) != int:
        try:
            Physics = int(Physics)
        except:
            print("The supplied value is not a number. Please try again")
            Physics = int(input("Enter the attendance for Physics: "))

    Chemistry = input("Enter the attendance for Chemistry: ")
    while type(Chemistry) != int:
        try:
            Chemistry = int(Chemistry)
        except:
            print("The supplied value is not a number. Please try again")
            Chemistry = input("Enter the attendance for Chemistry: ")
            
    IP = input("Enter the attendance for IP: ")
    while type(IP) != int:
        try:
            IP = int(IP)
        except:
            print("The supplied value is not a number. Please try again")
            IP = input("Enter the attendance for IP: ")
            

    try:
        sql="insert into attendance values('%s', '%d', '%d', '%d', '%d', '%d');" %(_Date_, English, Math, Physics, Chemistry, IP)
        cursor.execute(sql)
        connection.commit()
    except:
        print(".\n"*10)
        print(f"The supplied date {_Date_} already exists")
        print("Try entering a different date")


def ent2():
    import pymysql

    connection = pymysql.connect(host='localhost',user='root',password='Admin',db='XII_Project')
    cursor = connection.cursor()

    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    err = ["00","32","33","34","35","36","37","38","39"]
    Day = input("Enter the Date (DD):  ")
    
    while len(Day) != 2:
        print("Please check the given format and try again")
        Day = input("Enter the Date (DD):  ")
    
    x = False
    while x == False:
        if Day[0] not in numbers[0:4]:
            print("The supplied value is not a valid date. Please try again")    
            Day = input("Enter the Date (DD):  ")
            
        
        elif Day[1] not in numbers:
            print("The supplied value is not a valid date. Please try again")    
            Day = input("Enter the Date (DD):  ")
            
        
        elif Day in err:
            print("The supplied value is not a valid date. Please try again")
            Day = input("Enter the Date (DD): ") 
            
        else:
            x = True
        
    Day = str(Day)
 
    Months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    Month = input("Enter the Month (MM):  ")
    x = False
    while x == False:

        while Month not in Months:
            print("The supplied value is not a valid month. Please try again")    
            Month = input("Enter the Month (MM):  ")
            
        if Month in Months:
            x = True
        


    Year = input("Enter the Year (YYYY):  ")
    while type(Year) != int:
        try:
            Year = int(Year)
        except:
            print("The supplied value is not a number. Please try again")    
            Year = input("Enter the Year (YYYY):  ")
    Year = str(Year)

    
    _Date_ = Year + "-" + Month + "-" + Day
    print(_Date_)
    
       
    English = input("Enter the number of classes taken for English:")
    while type(English) != int:
        try:
            English = int(English)
        except:
            print("The supplied value is not a number. Please try again")
            English = input("Enter the number of classes taken for English:")
            
    Math = input("Enter the number of classes taken for Math: ")
    while type(Math) != int:
        try:
            Math = int(Math)
        except:
            print("The supplied value is not a number. Please try again")
            Math = input("Enter the number of classes taken for Math: ")
            
    Physics = input("Enter the number of classes taken for Physics: ")
    while type(Physics) != int:
        try:
            Physics = int(Physics)
        except:
            print("The supplied value is not a number. Please try again")
            Physics = int(input("Enter the number of classes taken for Physics: "))

    Chemistry = input("Enter the number of classes taken for Chemistry: ")
    while type(Chemistry) != int:
        try:
            Chemistry = int(Chemistry)
        except:
            print("The supplied value is not a number. Please try again")
            Chemistry = input("Enter the number of classes taken for Chemistry: ")
            
    IP = input("Enter the number of classes taken for IP: ")
    while type(IP) != int:
        try:
            IP = int(IP)
        except:
            print("The supplied value is not a number. Please try again")
            IP = input("Enter the number of classes taken for IP: ")
            

    try:
        sql="insert into dailystats values('%s', '%d', '%d', '%d', '%d', '%d');" %(_Date_, English, Math, Physics, Chemistry, IP)
        cursor.execute(sql)
        connection.commit()
    except:
        print(".\n"*10)
        print(f"The supplied date {_Date_} already exists")
        print("Try entering a different date")

def ent3():
    import pymysql

    connection = pymysql.connect(host='localhost',user='root',password='Admin',db='XII_Project')
    cursor = connection.cursor()

    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    err = ["00","32","33","34","35","36","37","38","39"]
    Day = input("Enter the Date (DD):  ")
    
    while len(Day) != 2:
        print("Please check the given format and try again")
        Day = input("Enter the Date (DD):  ")
    
    x = False
    while x == False:
        if Day[0] not in numbers[0:4]:
            print("The supplied value is not a valid date. Please try again")    
            Day = input("Enter the Date (DD):  ")
            
        
        elif Day[1] not in numbers:
            print("The supplied value is not a valid date. Please try again")    
            Day = input("Enter the Date (DD):  ")
            
        
        elif Day in err:
            print("The supplied value is not a valid date. Please try again")
            Day = input("Enter the Date (DD): ") 
            
        else:
            x = True
        
    Day = str(Day)
 
    Months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    Month = input("Enter the Month (MM):  ")
    x = False
    while x == False:

        while Month not in Months:
            print("The supplied value is not a valid month. Please try again")    
            Month = input("Enter the Month (MM):  ")
            
        if Month in Months:
            x = True
        


    Year = input("Enter the Year (YYYY):  ")
    while type(Year) != int:
        try:
            Year = int(Year)
        except:
            print("The supplied value is not a number. Please try again")    
            Year = input("Enter the Year (YYYY):  ")
    Year = str(Year)

    _Date_ = Year + "-" + Month + "-" + Day
    print(_Date_)
    
    print("For the following entries, please use the given format")
    print("'P' for Present \n'A' for Absent")
    valid_responses = ["P","A"]    
    
    English = input("English: ")
    English = English.upper()
    while English[0] not in valid_responses:
        print("The supplied value is not consistent with the given format. Please try again")
        English = input("English:")
        English = English.upper()
        
            
    Math = input("Math: ")
    Math = Math.upper()
    while Math[0] not in valid_responses:
        print("The supplied value is not consistent with the given format. Please try again")
        Math = input("Math:")
        Math = Math.upper()
        
    Physics = input("Physics: ")
    Physics = Physics.upper()
    while Physics[0] not in valid_responses:
        print("The supplied value is not consistent with the given format. Please try again")
        Physics = input("Physics:")
        Physics = Physics.upper()
        
    Chemistry = input("Chemistry: ")
    Chemistry = Chemistry.upper()
    while Chemistry[0] not in valid_responses:
        print("The supplied value is not consistent with the given format. Please try again")
        Chemistry = input("Chemistry:")
        Chemistry = Chemistry.upper()
        
    IP = input("IP: ")
    IP = IP.upper()
    while IP[0] not in valid_responses:
        print("The supplied value is not consistent with the given format. Please try again")
        IP = input("IP:")
        IP = IP.upper()
            

    try:
        sql="insert into teachers values('%s', '%s', '%s', '%s', '%s', '%s');" %(_Date_, English, Math, Physics, Chemistry, IP)
        cursor.execute(sql)
        connection.commit()
    except:
        print(".\n"*10)
        print(f"The supplied date {_Date_} already exists")
        print("Try entering a different date")

if __name__ == "__main__":
    userint = input("What dataset would you like to add to?\n1. Attendance \n2. Classes: \n3. Teachers Attendance \n")
    if userint == "1" or userint[0].lower() == "a":
        ent1()
    elif userint == "2" or userint[0].lower() == "c":
        ent2()
    elif userint == "3" or userint[0].lower() == "t":
        ent3()
    else:
        print("Please enter a valid input and try again later")
        
        
