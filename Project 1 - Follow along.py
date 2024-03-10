MAX_LINES = 3 #constant value

def deposit(): #collects user input
        while True:
            amount = input("What would you like to deposit? £") # user inputs amount and amount stored as a variable
            if amount.isdigit(): #this checks that it's a whole number
                amount = int(amount) #convert this to an integer data type
                if amount > 0: #if greater than zero then break loop
                    break
                else: #if not greater than zero then return the below text
                    print("Amount must be greater than.")
            else: #if not a number then return this
                print("Please enter a number.")
                
            return amount #this will return the value that is stored in amount variable from user input

def get_number_of_lines():
            while True:
                lines = input("Enter the number of lines to bet on:(1-" + str(MAX_LINES) +")? ") 
                if lines.isdigit(): #this checks that it's a whole number
                    lines = int(lines) #convert this to an integer data type
                    if amount > 0:
                            break
                    else:
                        print("amount must be greater than 0.")
                else:
                    print("Please enter a number.")

                
            return amount 


def main():        
    balance = deposit() #this runs the deposit function
    lines = get_number_of_lines()
    print(balance, lines)
main()
