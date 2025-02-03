#!python3
# Volume Calculator
# Feel free to rename your variables
import sys

def title():
    print("Calculate your taxes")
     # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    return None

def instructions():
    print("Enter your income to have your taxes calculated")
    input("Your Income: ")    
    # output parameters: None
    # Author:
    # Modified:
    return None



def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    def main():
   
        try:
            print("Welcome")

            user_input = input("Do you want to exit the program? (y/n): ")
            if user_input.lower() == "y":
                exit_program()

        except Exception as e:
            print(f"An error occurred: {e}")
            exit_program()

        def exit_program():
            print("Exiting the program...")
            sys.exit(0)


if __name__ == "__main__":
    main()
    