#deposit function
def deposit(amount):
    deposit_amount = input("Enter Deposit Amount")
    updateBalance = initial_amount+deposit_amount
    
    return updateBalance

#withdraw function
def withdraw(amount):
    withdraw_amount = input("Enter withdraw Amount")
    try:
        if withdraw_amount>=initial_amount:
            print ("Cannot Withdraw")
        else:
            print("Withdraw successful")
    except:
        print ("Input Value")
    
    updatedBalance= initial_amount - withdraw_amount
    
    return updatedBalance
        
#get balance
def getBalance():
    return amount

#transaction history
def transactionHistory():
    transaction_history = ["transfer to hihi","transferred to koko"]
    print(transaction_history)

#init amount
initial_amount = 50000

#Function Choosing
choice=input("""choose function
      1.deposit
      2.withdraw
      3.get balance
      4.Transcation History
      5.exit
      """)

if choice== 1:
    deposit()
elif choice== 2:
    withdraw()
elif choice==3:
    getBalance()
elif choice==4:
    transaction_history()
else:
    exit





