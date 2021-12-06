import sys
import mysql.connector
import smtpd
from time import sleep
import os
#--------------MYSQL------------------------------------
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="iptcfinals"
)
myc=mydb.cursor()
#--------------MYSQL------------------------------------
app=True
status = ""
def displayMenu():
    print("################################################")
    status = input("WELCOME TO DJOYOFBAKING! \nAre you registered user? y/n? Press q to quit").replace(" ","")
    print("################################################")
    if status == "y":
        os.system('cls')
        oldUser()
    elif status == "n":
        os.system('cls')
        newUser()
    elif status=="q":
        app=False
        os.system('cls')
        sys.exit("Exit Successfully")

def newUser():
    bool2=True
    bool3=True
    gmail = "False"
    addr = input("Address:")
    while bool2==True:
        username=input("Username:").replace(" ","")
        sql2="select * from customer where username= %s"
        myc.execute(sql2,[(username)])
        result2=myc.fetchall()
        if "@" in username or "#" in username or "$" in username or "*" in username or "%" in username or "&" in username or "|" in username or ";" in username or ":" in username or "[" in username or "]" in username or "'" in username or len(username)==0:
            print("Special characters are not allowed. Try again")
        else:
            if result2:
                for i in result2:
                    print("Username already taken please try again")
                    break
            else:
                bool2=False
    while bool3==True:
        createLogin = input("add Email Address: ").strip()
        sql = "select * from customer where emailadd = %s "
        myc.execute(sql, [(createLogin)])
        results = myc.fetchall()
        if "@gmail.com" in createLogin:
            gmail = "True"
            if results:
                for i in results:
                    print("\nEmail Address already exist! Please Try again\n")
                    break
            else:
                bool3=False
        else:
            print("@gmail.com is required")

    createPassw = input("Create password: ")
    if gmail=="True":
        sql = "INSERT INTO customer (address, emailadd, password,username) VALUES (%s,%s, %s,%s)"
        sql2="CREATE TABLE {0}(item varchar(250),price int,qty int)".format(username)
        val = (addr, createLogin, createPassw,username)
        myc.execute(sql2)
        myc.execute(sql, val)
        mydb.commit()
        os.system('cls')
        print(myc.rowcount, "record inserted.")
        print("\nUser created\n")
    else:
        print("Something's Wrong. Please Try again")
        os.system('cls')

def oldUser():
    login = input("Enter Email Address: ").replace(" ","")
    passw = input("Enter password: ")
    sql="select * from customer where emailadd = %s and password = %s"
    myc.execute(sql,[(login),(passw)])
    results=myc.fetchall()
    if results:
        for i in results:
            print("\nLogin successful!\n")
            firstPage()
            break
    else:
        print("\nUser doesn't exist or wrong password!\n")
def printOption():
    print("#####################################\n")
    print("[0]Search Item\n")
    print("[1]View Cart\n")
    print("[2]Buy Items\n")
    print("[3]Log Out\n")
def firstPage():
    boolean1=True
    printOption()
    while boolean1==True:
        user_input=input(":")
        if(user_input=="0"):
            print("Just Press Enter if you want to go back\nPlease type name of item you want to search\n")
            user_input2=input(":")
            if user_input2=="":
                os.system('cls')
                firstPage()
            else:
                print("Item not found!")
                os.system('cls')
                firstPage()
        elif(user_input=="1"):
            print("Just Press Enter if you want to go back\nYour Cart:\n")
            user_input3=input(":")
            if user_input3=="":
                os.system('cls')
                firstPage()
        elif(user_input=="2"):
            bool1 = True
            bool2 = True
            while bool1:
                os.system('cls')
                print("Just Press Enter if you want to go back\nCode Item\tItem Price \t\t\tItem Name")
                printItem()
                ChooseI=input(":").replace(" ","")
                if ChooseI=="1":
                    while bool2:
                        print("[0] Add to cart")
                        print("[1] Place order")
                        print("[Enter] Back")
                        Choose2=input(":").replace(" ","")
                        if Choose2=="0":
                            print("Added to Cart")
                            firstPage()
                        elif Choose2=="1":
                            print("Item is in process")
                            firstPage()
                        elif len(Choose2)==0:
                            os.system('cls')
                            firstPage()
                        else:
                            print("invalid input")
                            sleep(2.5)
                elif ChooseI=="2":
                    while bool2:
                        print("[0] Add to cart")
                        print("[1] Place order")
                        print("[Enter] Back")
                        Choose2=input(":").replace(" ","")
                        if Choose2=="0":
                            print("Added to Cart")
                            firstPage()
                        elif Choose2=="1":
                            print("Item is in process")
                            firstPage()
                        elif len(Choose2)==0:
                            os.system('cls')
                            firstPage()
                        else:
                            print("invalid input")
                            sleep(2.5)
                elif ChooseI=="3":
                    while bool2:
                        print("[0] Add to cart")
                        print("[1] Place order")
                        print("[Enter] Back")
                        Choose2=input(":").replace(" ","")
                        if Choose2=="0":
                            print("Added to Cart")
                            firstPage()
                        elif Choose2=="1":
                            print("Item is in process")
                            firstPage()
                        elif len(Choose2)==0:
                            os.system('cls')
                            firstPage()
                        else:
                            print("invalid input")
                            sleep(2.5)
                elif len(ChooseI)==0:
                    os.system('cls')
                    firstPage()
                else:
                    print("Invalid Input")

        elif user_input=="3":
            boolean1 = False
            print("Log out success")
            os.system('cls')
            displayMenu()
        else:
            print("Invalid Input!")
            os.system('cls')
            firstPage()

def printItem():
    myc.execute("SELECT * FROM items")
    result=myc.fetchall()
    j=0
    for i in result:
        print(
            f"{i[0]:<15} {i[2]:<15} {i[1]:>15}"
        )


while app==True:
    displayMenu()

