class BankSystem:
    def __init__(self,acc_no,pin,balance=0):
        self.acc_no = acc_no
        self.pin = pin
        self.balance = balance


    def login(self,acc_no,pin):
        if acc_no == self.acc_no and pin == self.pin:
            print("login successfull")
            return True
        else:
            print("invalid account number or pin")
            return False

    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(amount,"is deposited to your account\n your current balance is: ",self.balance)
        else:
            print("the minimum deposit amount is Rs1")


    def withdraw(self,amount):
        if amount>0 and amount<= self.balance:
            self.balance-=amount
            print("withdrawal of RS:",amount,"is successfull\n your current balance is:",self.balance)
        else:
            print("invalid withdrawal amount or insufficient balance")


    def balance_check(self):
        print("your current balance is:",self.balance)


    def change_pin(self, new_pin):
        self.pin = new_pin
        print("Your pin has been successfully changed")

sample=BankSystem(987654321,1234,25000)
        


print("WELCOME TO STATE BANK OF KERALA")
print(" Please Login")
acc_no = float(input("Enter your account number:"))
pin = float(input("Enter your pin"))
if sample.login(acc_no,pin):
    print("Services:")
    print("1.Deposit")
    print("2.Withdrawal")
    print("3.Balace check")
    print("4.Change pin")
    service = float(input("Please select a service:"))
    if service==1:
        amount = float(input("enter the amount"))
        sample.deposit(amount)
    elif service==2:
        amount = float(input("Enter the amount:"))
        sample.withdraw(amount)
    elif service==3:
        sample.balance_check()
    elif service==4:
        new_pin=float(input("Enter your new pin:"))
        sample.change_pin(new_pin)
    else:
        print("invalid choice\n please select a choice 1/2/3/4")
       