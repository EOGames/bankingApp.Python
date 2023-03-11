class Bank:
    totalbalance = 0.00
    def Deposit(self,amount):
        self.totalbalance = self.totalbalance+amount
        return self.totalbalance
    
    def Withdraw(self,amount):
        self.totalbalance = self.totalbalance-amount
        return self.totalbalance
    


app = Bank()
#balance = 0.00;
while True:
   ask = input("Please Enter D for deposit and W for witdraw ")

   if (ask.lower()=="d"):
         #deposit
         amount = input("Enter Money You Want To Submit ")
         amount = float(amount)
         balance =  app.Deposit(amount)
         print("Balance After Deposit ",balance)     
   elif (ask.lower()=="w"):
         #Withdraw
         amount = input("Enter Money You Want To Withdraw ")
         amount = float(amount)
         if (amount > balance):
             print(f"You Don't have {amount} Money Your Balance is {balance}")
         else: 
            balance = app.Withdraw(amount)
            print ("Balance after Withdraw ",balance)
   
        