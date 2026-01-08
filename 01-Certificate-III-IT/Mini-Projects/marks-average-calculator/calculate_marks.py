# Program to calculate sum and average marks for 5 subjects

print("Program to calculate sum and average marks for 5 subjects") # Introduce what the program is about
print("=" * 57, "\n") # Make the program easier to read

marksList = [] # The instructions require to ask the user to input the marks for the five subjects in a list, so define an empty list for input marks.
totalSubjects = 5 # The user is about to enter 5 marks for 5 subjects.
i = 1 # declare a counter variable used in while loop to count number of marks/subjects

print("please enter your 5 marks below") # The trainee uses gap between their code. That is good. Makes the code easy to read.

while True: # Use while loop here. If user inputs an invalid number, they need to re-enter a non-negative integer (between 0 and 100 inclusive) until 5 valid marks are input.

    # # read 5 inputs
    # mark1 = int(input("enter mark 1: ")) #The trainee should not define 5 variables for 5 marks, then create list with the 5 marks.
    # mark2 = int(input("enter mark 2: ")) #The trainee should create an empty list first, then ask the user to input marks in that list according to the requirement.
    # mark3 = int(input("enter mark 3: "))
    # mark4 = int(input("enter mark 4: "))
    # mark5 = int(input("enter mark 5: "))

    # #create array/list with five marks
    # marksList = [mark1, mark2, mark3, mark4, mark5]

    mark = input(f"\nPlease enter mark {i} (an integer between 0 and 100 inclusive) for subject {i} out of {totalSubjects} subjects: ") # Ask user to input a non-negative integer as mark for each subject.

    # There is no data validation for input values in the trainee's original code.
    # Data validation should be incorporated in the code to allow only an integer between 0 and 100 inclusive as a valid input according to the instructions.
    # The trainee's original code accepts any integer (even if it's bigger than 100 or smaller than 0); the trainee's original program will throw an error when the input is a non-integer instead of displaying an error message. These area needs to be corrected.
    
    if mark.isdigit(): # Here I first use data validation to check if the mark that user has input is a non-negative integer represented as a string.
                     
        mark = int(mark) # If the mark the user has input is a non-negative integer represented as a string, convert the string to integer.

        if mark >= 0 and mark <= 100: # Then, if the user input a non-negative integer represented as a string, I use data validation to check if the input is between 0 and 100 inclusive.
                                      # The trainee's original code did not have this data validation.
                                      # If the user entered a non-negative integer but it is not between 0 and 100 inclusive, the trainee's original code would still accept this input, which should have been treated as an invalid input.

            marksList.append(mark) # if the input is between 0 and 100 inclusive, then add the mark to the marksList.

            i = i + 1 # if a valid mark is entered, use the counter i to move to next input

            if i == totalSubjects + 1: # check if 5 valid marks are input, if so, display the list, sum of marks and average mark.

                # # print the array/list
                # print(marksList)   #The trainee's original code to print list is not wrong. I improved the readability for the code.

                print(f"\nThe marks you entered for 5 subjects are: {marksList}.")
                # #calculate the sum and average
                # sumOfMarks = sum(marksList)  # The trainee's original code to calculate the sum and average is not wrong.
                # averageOfMarks = sum(marksList)/5

                sumOfMarks = sum(marksList) 
                print(f"\nThe sum of your marks is: {sumOfMarks}.")

                averageOfMarks = sumOfMarks / totalSubjects #I have defined the total number of subjects in the beginning of the program for the code to be better understood.
                print(f"\nThe average of your marks is: {averageOfMarks}.")

                # #display results
                # print("The sum of your marks is: "+str(sumOfMarks)) # The trainee's original code for display results is not wrong. I improved the code for simplicity.
                # print("The average of your marks is: "+str(averageOfMarks))

                break # after displaying the list, sum of marks and average mark if 5 valid marks are input, get out of the loop.

        else: # I add an error handling here. If the user entered a non-negative integer but it is not between 0 and 100 inclusive, display an error message. 
              # The trainee's original code did not have this data validation.
              # If the user entered a non-negative integer but it is not between 0 and 100 inclusive, the trainee's original code would still accept this input, which should have been treated as an invalid input.

            print("\nError! Invalid input! The mark you entered is out of range (0 to 100 inclusive). Please re-enter an integer between 0 and 100 inclusive.")
            continue # Return to the beginning of the while loop. That will ask the user to re-enter an integer between 0 and 100 inclusive until it's valid.

    else:# I add an error handling here. If the user entered a non-negative integer, display an error message.
         # The trainee's original code did not have this data validation. If the user's input is not an integer, the trainee's original program would throw an error instead of displaying an error message.

        print("\nError! Invalid input! You did not enter a non-negative integer. Please re-enter an integer between 0 and 100 inclusive.")
        continue # Return to the beginning of the while loop. That will ask the user to re-enter an integer between 0 and 100 inclusive until it's valid.

print("\nEnd of program.") # I add this code for readability.

# End of program.
    




