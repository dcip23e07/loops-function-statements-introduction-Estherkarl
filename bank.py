def atm_machine():
    balance = 1000
    min_withdrawal = 10
    max_withdrawal = 500
    
    while True:
        choice = input("Do you want to withdraw money? (yes/no): ")
        
        if choice.lower() == "no":
            print("Thank you for using our ATM. Have a nice day!")
            break
        
        elif choice.lower() == "yes":
            amount = float(input("How much money do you want to withdraw? "))
            
            if amount < min_withdrawal:
                print("Sorry, the minimum withdrawal amount is", min_withdrawal)
            
            elif amount > max_withdrawal:
                print("Sorry, the maximum withdrawal amount is", max_withdrawal)
            
            elif amount > balance:
                print("Sorry, you do not have enough balance to withdraw", amount)
            
            else:
                balance -= amount
                print("Withdrawal successful. Your remaining balance is", balance)
        
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
    print("It was a pleasure!")

atm_machine()

