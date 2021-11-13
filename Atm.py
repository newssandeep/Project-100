class ATM:
    def __init__(self, cnum, pnum):
        self.cnum = cnum
        self.pnum = pnum
        self.money = 0
    
    def accountInfo(self):
        print(f"Your account card number is {self.cnum}, your account pin number is {self.pnum}, and you have {self.money} dollars in your account")
    
    def withdraw(self, a):
        if a > self.money:
            return "You don't have enough money to complete that withdrawal!"
        if input("Enter your card number:\n") != self.cnum:
            return "Incorrect Card Number!"
        self.money -= a
        return "Withdrawal Complete!"
    def deposit(self, a):
        if input("Enter your card number:\n") != self.cnum:
            return "Incorrect Card Number!"
        self.money += a
        return "Deposit Complete!"

account = ATM(input("Enter Your Accounts Card Number:\n"), input("Enter Your Accounts Pin Number:\n"))
account.accountInfo()
running = True
while running:
    action = input("Would you like to do a withdrawal(1), deposit(2), or view account details(3)? (Enter number for action and enter 'q' to quit)\n")
    if (action == "1"):
        print(account.withdraw(int(input("How much money would you like to withdraw?\n"))))
    elif (action=="2"):
        print(account.deposit(int(input("How much money would you like to deposit?\n"))))
    elif (action=="3"):
        account.accountInfo()
    elif (action=="q"):
        running = False
    else:
        print("Invalid Input! Try Again")

print("Thank you for using the ATM")