#!python3
# Volume Calculator
# Feel free to rename your variables
#total net income
#calculate ei
#calculate cpp
#calculate federal tax

def title():
    print("Hello")
    print ("This is a tax calculator for residents in British Columbia")
    return None

def instructions():
    print("First you have to enter your income")    
    print("I will then calculate your provincial and federal taxes")
    # output parameters: None
    # Author:
    # Modified:
    return None

income = input("income: ")

def ei():
    if 0 <= income <= 65700:
        return (1.64)*income
    return 0
def cpp():
    if 0 <= income <= 67800:
        cpp=0.0595*income
    return None

def ptax():
        print('BC Tax brackets')
        if 0 <= income <= 49279:
            tax = income*(0.0506)
        if 49279.01 <= income < 98560:
            tax = income*(0.077) + tax
        if 98560.01 <= income < 113158:
            tax = income*(0.105) + tax
        if 113158.01 <= income < 137407:
            tax = income*(0.1229) + tax
        if 137407.01 <= 186306:
            tax = income*(0.147) + tax
        if 186306.01 <= income < 259829:
            tax = income*(0.168)
        if income > 259829.01:
            tax= income in range(259829.01,1000000000000000000000000000000000000000000000000000000)*(.205) + tax
        print (tax)
        return None

def Ftax():
    if 0 <= income <= 57375:
        tax = income*(0.15)
    if 57375.01 <= 114750:
        tax= income*(0.205) + tax
    if 114750.01 <= income <= 177882:
        tax= income*(0.26) + tax
    if 177882.01 <= income <= 253414:
        tax= income*(0.29) + tax
    if income > 253414.01:
        tax = income*(0.33) + tax
    return None
def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    title()
    while True:
        # keep giving options to choose menu options until they choose to exit
        pass

if __name__ == "__main__":
    title()
    instructions()
