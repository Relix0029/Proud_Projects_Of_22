def rt():


    import pymysql
    import pandas as pd
    import sys
    connection = pymysql.connect(host='localhost',user='root',password='Admin',db='xii_project')
    cursor=connection.cursor()
    
    sql="select * from teachers order by Date;"
    cursor.execute(sql)
    
    x=cursor.fetchall()
    

    if x == ():
        print("Sorry, no previous records found")
        print("Please enter some data and try again later")
        sys.exit()
    
    x=list(x)
    y=[]
    for i in x:
        y.append(list(i))
        
    #print(y)
    
    z=[]
    for u in y:
        for v in u:
            z.append(v)
    #print(z)
    

                
    Date=[]
    a=0
    while True:
        
        try:
            Date.append(z[a])
            a+=6
            
        except:
            break
        
    
    English=[]
    a=1
    while True:
        
        try:
            English.append(z[a])
            a+=6
            
        except:
            break
        
    
    Math=[]
    a=2
    while True:
        
        try:
           Math.append(z[a])
           a+=6
            
        except:
            break
        
    
    Phy=[]
    a=3
    while True:
        
        try:
            Phy.append(z[a])
            a+=6
            
        except:
            break
        
    
    Chem=[]
    a=4
    while True:
        
        try:
            Chem.append(z[a])
            a+=6
            
        except:
            break
        
    
    IP=[]
    a=5
    while True:
        
        try:
            IP.append(z[a])
            a+=6
            
        except:
            break
        
    
        
    
    fdict={'Date': Date,
          'English':English,
          'Math':Math,
          'Physics':Phy,
          'Chemistry': Chem,
          'IP':IP}

    df=pd.DataFrame(fdict)
    return(df)

if __name__ == "__main__":
   rt()
