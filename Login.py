import sys
import mysql.connector
import smtpd
from time import sleep
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
        oldUser()
    elif status == "n":
        newUser()
    elif status=="q":
        app=False
        sys.exit("Exit Successfully")


def newUser():
    gmail = "False"
    addr = input(":").replace(" ", "")
    createLogin = input("add Email Address: ").replace(" ","")
    sql = "select * from customer where emailadd = %s "
    myc.execute(sql, [(createLogin)])
    results = myc.fetchall()
    if "@gmail.com" in createLogin:
        gmail = "True"
    if results:
        for i in results:
            print("\nEmail Address already exist!\n")
            break
    else:
        createPassw = input("Create password: ")
        if gmail=="True":
            sql = "INSERT INTO customer (address, emailadd, password) VALUES (%s,%s, %s)"
            val = (addr, createLogin, createPassw)
            myc.execute(sql, val)
            mydb.commit()
            print(myc.rowcount, "record inserted.")
            print("\nUser created\n")
        else:
            print("@gmail.com is required")


def oldUser():
    login = input("Enter login name: ").replace(" ","")
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
def firstPage():
    boolean1=True
    print("#####################################\n")
    print("[0]Search Item\n")
    print("[1]View Cart\n")
    print("[2]Add to Cart\n")
    print("[3]Log out\n")
    while boolean1==True:
        user_input=input(":")
        if(user_input=="0"):
            print("Just Press Enter if you want to go back\nPlease type name of item you want to search\n")
            user_input2=input(":")
            if user_input2=="":
                firstPage()
            else:
                print("Item not found!")
                sleep(1.5)
                firstPage()
        elif(user_input=="1"):
            print("Just Press Enter if you want to go back\nYour Cart:\n")
            user_input3=input(":")
            if user_input3=="":
                firstPage()
        elif(user_input=="2"):
            print("Just Press Enter if you want to go back\nItem Name\tPrice")
            print("Enzaimada\t30 Peses\n")
            user_input4=input(":")
            if user_input4=="":
                firstPage()
        elif user_input=="3":
            boolean1 = False
            print("Log out success")
            displayMenu()
        else:
            firstPage()
            print("Invalid Input!")


while app==True:
    displayMenu()

