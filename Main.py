# Bank Record System can keep the information account type, account opening form, Deposit, 
# Withdrawal, and searching the transaction, Transaction report, Individual account opening form, Group account as a record
from classes import user
from classes import Linkedlist
import sys




click = 0
user1 = user('','')
admin = user('admin','admin')
data = Linkedlist()


    
while click != 3:
    print("======================Welcome to our banking system========================")
    print("")
    print("1.user")
    print("2.Admin")
    print("3.Exit")
    click = int(input("Enter value: "))

    if click == 1:
        print("a. register")
        print("b. login")
        select = input("select options: ")
        
        if select == 'a':
            user1.username = input("please create username: ")
            user1.password = input("please create password: ")
            data.insertBeginning(user1.username,user1.password)
            data.print_list()
    
        if select == 'b':
            
            username = input("Please input username: ")
            password = input("please input password: ")
            search = data.search_account(username,password)
            if search is True:
                print('Login success')
                
    
    if click == 2:
        username = input("please input username: ")
        password = input("please input password: ")
        if (username == admin.username) and (password == admin.password):
            print ("welcome back Admin")


    
    if click == 3:
        sys.exit()
            



