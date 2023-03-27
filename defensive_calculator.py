# import relevant library
import os

def calculator():
    # Create try else block for valid numeric input
    while True:
        try:
            string = input("enter two numbers with a space in between: ")
            # the float() is the test of whether it will be a true numeric value
            num1,num2 = tuple([float(i) for i in string.split(" ")])
            break
        # if the float() fails then the tuple unpacking wont happen which will print the below. Since the loop has not broken it will ask for a valid number again.
        # So code wont break
        except ValueError:
            print("You did not enter a valid number.")
    
    # create an operation selection function as this will be used to find a valid operator and in the zero division error exception
    def operation_selector():
        # Create an exception object as a proxy for operation in ['+','-','*','/'] statement.
        incorrect_operation = True
        while incorrect_operation:
            try:
                operation = input("Please enter an operation of your choice from this list +,-,*,/ \n")
                if operation in ['+','-','*','/']:
                    incorrect_operation = False # break loop if condition is true
            except Exception:
                print("You did not enter a valid operation. Try again") # since the function is assigned to a variable it wont actually print this out.
                # regardless since while loop has not broken it will ask to input again.
        return operation


    while True: # final while loop block that is there to continually loop through the try else for zero division error at the end.
        operation = operation_selector()  
        if operation == "+":
            output = num1 + num2
            break
        elif operation == "-":
            output = num1 - num2
            break
        elif operation == "*":
            output = num1 * num2
            break
        else:
            try:
                output = num1 / num2
                break
            except ZeroDivisionError:  # once this error occurs the loop will return to the operation_selector() and continue until correct operation is selected.
                print("The denominator cannot be zero. Please choose another operation!")

    return f'{num1}{operation}{num2} = {output}'



def user_interface():
    # Exception object acting as proxy for user input question asking whether they want more calculations or if they want to stop
    switch_on = True
    file = input("Before we start our calculation, please choose the name for the file in which you would like to save the calculations in.\n")
    if not os.path.exists(os.path.join('./T24/',file + '.txt')):  # if defensively checks if file does not exist
        file = open(os.path.join('./T24/',file + '.txt'),'w+') # creates it if it does not
        while switch_on: 
            output_string = calculator()  # asks for calculation
            file.write(output_string + '\n')  # writes to text file
            switch_on = input("Would you like to continue or stop? write TRUE to continue or FALSE to stop?\n").lower() # asks if they want to continue
            if switch_on == "false":
                switch_on = False # breaks while loop if they dont want to continue
    else:  # if file exists.....
        with open(os.path.join('./T24/',file + '.txt'),'a+') as f:  # append to file when writing
            while switch_on:  
                output_string = calculator()
                f.write(output_string + '\n')
                switch_on = input("Would you like to continue or stop? write TRUE to continue or FALSE to stop?\n").lower()
                if switch_on == "false":
                    switch_on = False

def final(): 
    question = input("Would you like to do a new calculation or view your calculations from a file? Please enter 1 for the first option and 2 for the second.\n")
    while question not in ['1','2']:
        print('You did not choose a valid option. Try again.')
        question = input("Would you like to do a new calculation or view your calculations from a file? Please enter 1 for the first option and 2 for the second.\n")
    if question == '1':
        user_interface()
    else:
        file = input("Please type the name of the existing file from which you want to see the calculations from.\n")
        while not os.path.exists(os.path.join('./T24/',file + '.txt')):
            file = input("Sorry, this file does not exist. Please type the name of the existing file from which you want to see the calculations from.\n")
        else:
            with open(os.path.join('./T24/',file + '.txt'),'r+') as f:
                content = f.readlines()
            for lines in content:
                print(lines)

        
        

final()
