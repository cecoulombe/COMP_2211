# Author: Caitlin Coulombe, T00756521
# Date: October 1, 2024
# Course: COMP 2211
#
# Assignment 1: Complete Questino 19 (Future Values) on page 283
#
# Question 19: Suppose you have a certain amount of money in a savings 
# account that earns compound monthly interest, and you ant to calculate 
# the amount that you will have after a specific number of months. The 
# formula is as follows:
# F = Px(1 + i)t
#   # F is the future value of the account after the specified time period
#   # P is the present value of the account
#   # i is the monthly interest rate
#   # t is the number of months
#
# Write a program that prompts the user to enter the account's present 
# value, monthly interest rate, and the number of months that the money 
# will be left in the account. The program should pass these values to 
# a function that returns the future value of the account, after the 
# specified number of months. The program should then display the account's 
# future value.
#

#---------------------------------------------------------------------
# main() executes the main logic of the program
#---------------------------------------------------------------------
def main():
    presValue = getPresentValue()
    print()
    intRate = getInterestRate()
    print()
    months = getMonths()
    print()

    futureValue = calcFutureValue(presValue, intRate, months)
    print(f"The future value of the account will be: ${futureValue:.2f}")

#---------------------------------------------------------------------
# getPresentValue() gets the present value of the account
#---------------------------------------------------------------------
def getPresentValue():
    # input validation: ensure the number is a positive float
    while True:
        try:
            value = float(input("Enter the current value of the account (positive amount): "))
            if(value <= 0):
                raise ValueError("Current value must be positive and nonzero.")
            return value
        except ValueError as e:
            print(e)
    

#---------------------------------------------------------------------
# getInterestRate() gets the interest rate of the account
#---------------------------------------------------------------------
def getInterestRate():
    # input validation to ensure a positive percent
    while True:
        try:
            rate = float(input("Enter the interest rate as a percent (0 - 100): "))
            if(rate < 0 or rate > 100):
                raise ValueError("Interest rate must be between 0 and 100.")
            return rate / 100
        except ValueError as e:
            print(e)

#---------------------------------------------------------------------
# getMonths() gets the amount of time the money will be left in the account
#---------------------------------------------------------------------
def getMonths():
    # input validation for a positive integer number of months
    while True:
        try:
            months = int(input("Enter the number of months the money will be left in the account: "))
            if(months < 0):
                raise ValueError("The number of months must be a positive integer.")
            return months
        except ValueError as e:
            print(e)
    

#---------------------------------------------------------------------
# calcFutureValue(presValue, intRate, months) calculates the future value of the account
#---------------------------------------------------------------------
def calcFutureValue(presValue, intRate, months):
    result = presValue * (1 + intRate) ** months
    return result



# call the main function
main()
