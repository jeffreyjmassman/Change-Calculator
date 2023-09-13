'''Main function that runs during script execution. no 'if __name__ == __main__' necessary since
this is a stand-alone script'''

def main():

    answer = str(input("Do you want to use the change calculator at this time? y/n: "))

    if answer.upper() == 'Y':
        print("Okay. Running calculator now.\n")
        change_calculator()

    elif answer.upper() == 'N':
        print("Okay, shutting down calculator.")

    else:
        print("Sorry, I could not interpret your answer. Please write only 'y' or 'n' into the terminal.")
        main()

    return 0

'''Function that calculates the change you owe to the customer, written in bills and coins. Note
    that this function does not include half dollars.'''

'''Determines whether or not to add an 's' at the end of the return string, e.g. "quarter" vs "quarters" '''

def add_s(number):

    if number == 1:
        return ''
    else:
        return 's'
    
'''Determines whether to add the word "penny" or "pennies" in the return string'''

def pennyOrPennies(number):

    if number == 1:
        return "Penny"
    else:
        return "Pennies"

def change_calculator():

    owed = float(input("How much is owed to you? "))
    given = float(input("How much were you given? "))

    if owed > given:
        print(f"The customer still owes you ${owed - given}. Ask for the difference and try again.")
        change_calculator()

    elif owed == given:
        print("The customer gave you the exact amount owed; no change necessary.")

    else:
        amounts = [100,50,20,10,5,1,0.25,0.1,0.05,0.01] # Canonical currency amounts (United States)
        currency = {0:"$100 Bill",1:"$50 Bill", 2:"$20 Bill", 3:"$10 Bill", 4:"$5 Bill", 5:"$1 Bill",
                    6: "Quarter", 7:"Dime", 8:"Nickel", 9:"Penny"}
        numbers = {} # Dictionary that stores the number of each type of currency we owe
        total = round(given - owed,2) # We round to minimize the occurrence of floating point errors

        for idx in range(10):
            amt = amounts[idx]
            number = total // amt
            numbers[idx] = int(number)
            total -= number * amt
            total = round(total, 2)

        print("\nYou owe:\n")

        for idx in range(10):
            amt = numbers[idx]
            if amt > 0:
                if idx == 9:
                    ret_str = str(amt) + " " + pennyOrPennies(amt) + "\n"  
                else:
                    ret_str = str(amt) + " " + currency[idx] + add_s(amt) + "\n"
                print(ret_str)

main()