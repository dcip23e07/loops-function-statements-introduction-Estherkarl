
current_balance: int = 500
minimum_withdrawal: int = 50
maximum_withdrawal: int = 10000


print("Welcome to Esther Bank, you can deposit and withdraw your money! ")


answer = input("\nDo you want to withdraw some money: ")

def hello():
    user_input: str = input("How much do you want to withdraw?: ")
    amount:int = int(user_input)
    current_balance = 500
    new_balance = current_balance - amount
    
    while current_balance:
        
         if amount < minimum_withdrawal:
             print("\nThe amount you wish to withdraw is less than the minimum amount to withdraw, please change the amount")
             import time
             time.sleep(1)
             break
        
         elif amount > maximum_withdrawal:
            print("\nThe amount you wish to withdraw is more than your current balance and more than the maximum amount to withdraw, please change the amount")
            import time
            time.sleep(1)
            break
         else:
             
            new_balance = int(current_balance - amount)
            if new_balance < 0 :
                print("\nThe amount you wish to withdraw is more than your current balance")
                import time
                time.sleep(1)
                break
        
            else:
            
             print("\nYour current balance is: "+str(new_balance))
             option = input("\nDo you want to perform another transaction?:")
    
            if option.lower().strip() == "no":
                    print("\n Process canceled, Have a nice day")
                    input("Press Enter To Close")
                    import time
                    time.sleep(1)
                    break
        
            elif option.lower().strip() =="yes":
                     hello()

        
            else:
                    option = input("\n It was a pleasure! ")
                    import time
                    time.sleep(1)
                    break
        
    
    return
             
             
                    
    return
    

while answer:
    
    if answer.lower().strip() == "no":
        print("\n Process canceled, Have a nice day")
        input("Press Enter To Close")
        import time
        time.sleep(1)
        break
        
    elif answer.lower().strip() =="yes":
        hello()
       
        
    else:
        answer = input("\nPlease enter 'yes' or 'no'.replay?: ")

   

    



