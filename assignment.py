#!python3
# Volume Calculator
# Feel free to rename your variables
#total net income
#calculate ei
#calculate cpp
#calculate federal tax

def title():
    return "Hello, this is a tax calculator for residents in British Columbia."

def instructions():
    return "First, you have to enter your income, and I will then calculate your provincial and federal taxes."

def income():
    while True:
        income = input("Enter your income or type 'exit' to quit: ")
        if income == "exit" or income == "EXIT":
            return None
        try:
            income = float(income)
            if income < 0:
                print("Enter a positive number.")
            else:
                return income
        except ValueError:
            print("Error accured try agian")

def ei(income):
    if income <= 65700:
        return 0.016 * income
    return 0.016 * 65700

def cpp(income):
    if income <= 67800:
        return 0.0595 * income
    return 0.0595 * 67800

def ptax(income):
    if income <= 49279:
        tax = income * 0.0506
    elif income <= 98560:
        tax = (49279 * 0.0506) + (income - 49279) * 0.077
    elif income <= 113158:
        tax = (49279 * 0.0506) + (49281 * 0.077) + (income - 98560) * 0.105
    elif income <= 137407:
        tax = (49279 * 0.0506) + (49281 * 0.077) + (16190 * 0.26) + (income - 113158) * 0.1229
    elif income <= 186306:
        tax = (49279 * 0.0506) + (49281 * 0.077) + (16190 * 0.26) + (24249 * 0.1229) + (income - 137407) * 0.147
    elif income < 259829:
        tax = (49279 * 0.0506) + (49281 * 0.077) + (16190 * 0.26) + (24249 * 0.1229) + (48896 * 0.147) + (income - 186306) * 0.168
    else:
        tax = (49279 * 0.0506) + (49281 * 0.077) + (16190 * 0.26) + (24249 * 0.1229) + (48896 * 0.147) + (73526 * 0.168) + (income - 259829) * 0.205
    return tax

def ftax(income):
    ftax = 0
    if income <= 57375:
        ftax = income * 0.15
    elif income <= 114750:
        ftax = (57375 * 0.15) + (income - 57375) * 0.205
    elif income <= 177882:
        ftax = (57375 * 0.15) + (57375 * 0.205) + (income - 114750) * 0.26
    elif income <= 253414:
        ftax = (57375 * 0.15) + (57375 * 0.205) + (63132 * 0.26) + (income - 177882) * 0.29
    else:
        ftax = (57375 * 0.15) + (57375 * 0.205) + (63132 * 0.26) + (75532 * 0.29) + (income - 253414) * 0.33
    return ftax

def main():
    print(title())
    print(instructions())
    
    while True:
        incomes = income()
        if income is None:
            print("You have exited the program.")
            break
        
        ptaxs = ptax(incomes)
        ftaxs = ftax(incomes)
        eis= ei(incomes)
        cpps = cpp(incomes)
        
        total = ptaxs + ftaxs + eis + cpps
        
        print(f"Your income:{income}")
        print(f"Provincial Tax:{ptaxs:.2f}")
        print(f"Federal Tax:{ftaxs:.2f}")
        print(f"EI: ${eis:.2f}")
        print(f"CPP: ${cpps:.2f}")
        print(f"Total Tax: ${total:.2f}")


if __name__ == "__main__":
    main()''
