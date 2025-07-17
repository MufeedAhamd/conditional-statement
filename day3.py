balance = 10000
limit = 1000
def deposite (amount):
    balance = balance + amount
    print(balance)

def withdraw (amount):
    if balance > limit :
           balance = balance - amount
           print(balance)

print('''Select the option for the activity 
         1 for Deposite
         2 for Withdraw
         3 for Balance check ''')
x = int(input(" Select your option"))
if x == 1 :
    amount = int(input("enter the your amount :"))
    print ("your amount")
    deposite(amount)
elif x == 2 :
    amount = int(input("enter the your amount :"))
    withdraw(amount)