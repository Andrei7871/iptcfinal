import sys
import mysql.connector
import smtpd
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
    status = input("WELCOME TO DJOYOFBAKING! \nAre you registered user? y/n? Press q to quit").replace(" ","")
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
            break
    else:
        print("\nUser doesn't exist or wrong password!\n")

while app==True:
    displayMenu()

