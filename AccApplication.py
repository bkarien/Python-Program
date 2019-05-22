import os
import AccountDetails
class AccountApplication:
    
    def Opt1(AccNo, Bal):
        print("You are to create",N,"accounts")
        index=0

        while index<N:
            while True:
                No=int(input("Please create Account Number: "))
                loop=0
                Check=False
                while loop<index:
                    if(AccNo[loop]==No):
                        Check=True
                        break

                    else:                        
                        Check=False
                    loop=loop+1
                if(Check==True or No<999 or No>9999):
                    print("Invalid Account Number")
                else:
                    AccNo.append(No)

                    while True:
                        Bl=float(input("Please enter Balance: K"))
                        if(Bl<1 or Bl>100000):
                            print("Invalid Amount")
                        else:
                            Bal.append(Bl)

                            break
                                            
                    break
            index=index+1
        os.system('cls')
        print("Transaction Complete")

    def Opt2(AccNo, Bal):
        if(AccNo==[]):
            print("You have no Accounts.\n\n")
            print("You have been redirected here to create your accounts")
            AccApp.Opt1(AccNo, Bal)
        else:
            print("These are all your Accounts' Details")
            for index in range(N):
                print(index+1,") Account Number: ",AccNo[index],"\n    Balance: K%.2f"%Bal[index])
    def Opt3(AccNo, Bal):
        if(AccNo==[]):
            print("You have no Accounts.\n\n")
            print("You have been redirected here to create your accounts")
            AccApp.Opt1(AccNo, Bal)
        else:
            loop=0
            for index in range(N):
                if(Bal[index]==1.0):
                    print(index+1,"Account Number: ",AccNo[index])
                    loop=loop+1
            if(loop==0):
                print("None of the Accounts have K1.00")
            else:
                print("\nThese are the Accounts that have K1.00")
    def Opt4(Bal):
        if(AccNo==[]):
            print("You have no Accounts.\n\n")
            print("You have been redirected here to create your accounts")
            AccApp.Opt1(AccNo, Bal)
        else:
            print("These are the Account Balances that are below Average.\n")
            Sum=0
            for index in range(N):
                Sum=Sum+Bal[index]
            Av=Sum/N
            for index in range(N):
                if(Bal[index]<Av):
                    print(index+1,"K%.2f"%Bal[index])
    def Opt5(AccNo, Bal):
        if(AccNo==[]):
            print("You have no Accounts.\n\n")
            print("You have been redirected here to create your accounts")
            AccApp.Opt1(AccNo, Bal)
        else:
            print("The account with the largest balance is;")
            loop=0
            for index in range(N):
                if(Bal[index]>loop):
                    loop=Bal[index]
            for index in range(N):
                if(loop==Bal[index]):
                    print(index+1,")Account Number: ",AccNo[index])
    def Opt6(AccNo, Bal):
        if(AccNo==[]):
            print("You have no Accounts.\n\n")
            print("You have been redirected here to create your accounts")
            AccApp.Opt1(AccNo, Bal)
        else:
            print("These are the Account Balances in decending order;")
            bl=[]
            for index in range(N):
                bl.append(Bal[index])
            bl.sort(reverse=True)
            for index in range(N):
                print("Balance: K%.2f"%bl[index])
    def Opt7(AccNo, Bal):
        if(AccNo==[]):
            print("You have no Accounts.\n\n")
            print("You have been redirected here to create your accounts")
            AccApp.Opt1(AccNo, Bal)
        else:
            while True:
                Bl=float(input("Enter amount to begin search: K"))
                loop=0
                if(Bl<1 or Bl>100000):
                    print("Invalid ammount")
                else:
                    for index in range(N):
                        if(Bl==Bal[index]):
                            print(index+1,") Account Number: ",AccNo[index])
                            loop=loop+1
                    if(loop==0):
                        print("There are no Accounts with K%.2f"%Bl)
                        break
                    else:
                        print("These are the Accounts with K%.2f"%Bl)
                        break
    def Opt8():
        while True:
            opt=int(input(""))
            if(opt==1):
                exit(0)
            elif(opt==2):
                os.system('cls')
                print("Welcome to the ID number Banking System")
                break
            else:
                print("Invalid Choice")
                

    def Account():
        Acc=Account
        AccNo=Account.AccountNo
        Bal=Account.Balance

    def AccApp():
        AccApp==0
        N=int(Account.maxValue)

print("Welcome to the ID number Banking Simulator")


while True:
    print("-----------\n Main Menu \n-----------")
    print("[1]Store Account Number and Balance")
    print("[2]Display All Account Numbers and Balances")
    print("[3]Display Account Number(s) with K1.00")
    print("[4]Display Account Balance(s) below average Balance")
    print("[5]Display Account with Largest Balance")
    print("[6]Display Account Balances in Descending Order")
    print("[7]Display Account Number(s) equal to given Balance")
    print("[8]Exit program")
    Opt=int(input("Choice: "))
    if(Opt>8 or Opt<1):
        os.system('cls')
        print("Invalid Choice")
    elif(Opt==1):
        os.system('cls')
        AccNo=[]
        Bal=[]
        AccApp.Opt1(AccNo, Bal)
    elif(Opt==2):
        os.system('cls')
        AccApp.Opt2(AccNo, Bal)
    elif(Opt==3):
        os.system('cls')
        AccApp.Opt3(AccNo, Bal)
    elif(Opt==4):
        os.system('cls')
        AccApp.Opt4(Bal)
    elif(Opt==5):
        os.system('cls')
        AccApp.Opt5(AccNo, Bal)
    elif(Opt==6):
        os.system('cls')
        AccApp.Opt6(AccNo, Bal)
    elif(Opt==7):
        os.system('cls')
        AccApp.Opt7(AccNo, Bal)
    elif(Opt==8):
        os.system('cls')
        print("Are you sure you want to exit?\n(Your data will not be saved)")
        print("~~Yes(1)~~No(2)~~")
        AccApp.Opt8()
