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
        elif 49279.01 <= income:
            tax= (49279 * 0.0506) + (income - 49279) * 0.077
        elif 98560.01 <= income:
            tax=(49279 * 0.0506) + (49281 * 0.077) + (income - 98560) * 0.105
        elif 113158.01 <= income:
            tax = (49279 * 0.0506) + (49281 * 0.077) + (16190 * 0.26) + (income - 113158 )*0.1229
        elif 137407.01 <= income:
            tax = (49279 * 0.0506) + (49281 * 0.077) + (16190 * 0.26) + (24249 * 0.1229 ) + (income- 134707)* 0.147
        elif 186306.01 <= income < 259829:
            tax = (49279 * 0.0506) + (49281 * 0.077) + (16190 * 0.26) + (24249 * 0.1229 ) + (48896 * 0.147) + (income - 186303)
        else:
            tax = (49279 * 0.0506) + (49281 * 0.077) + (16190 * 0.26) + (24249 * 0.1229 ) + (48896 * 0.147) + (73526 * 0.168) + (income - 259829)*0.205
        print (tax)
        return ptax

def income():
    input("enter income")
    return income



def Ftax():
    tax = 0
    if 0 <= income <= 57375:
        tax = income * 0.15
    elif income <= 114750:
        tax = (57375 * 0.15) + (income - 57375) * 0.205
    elif income <= 177882:
        tax = (57375 * 0.15) + (57375 * 0.205) + (income - 114750) * 0.26
    elif income <= 253414:
        tax = (57375 * 0.15) + (57375 * 0.205) + (63132 * 0.26) + (income - 177882) * 0.29
    else:
        tax = (57375 * 0.15) + (57375 * 0.205) + (63132 * 0.26) + (75532 * 0.29) + (income - 253414) * 0.33
    return Ftax
def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    title()
    instructions()
    if True:
        income = input("Enter your income or awnser exit to exit: ")
        if income == "exit":
            print("You have exited the program")
            return income
        
        try:
            ptax()
            print(ptax)
        except:
            print("Error has accured")

        

if __name__ == "__main__":
    main()
