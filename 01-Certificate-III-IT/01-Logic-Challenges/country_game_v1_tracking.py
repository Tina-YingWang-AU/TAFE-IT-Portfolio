# Program for Country-Capital matching Game
# first randomly pick a country. Then randomly prick another country from the original list. If the second country is the same as the first country, randomly pick another country
# again, until it's a different country. During the process, ask the user if they want to play next country, if not, program ends.
# When all the countries in the list have been picked once, ask the user if they want to play the list again, if not, program ends.

print("\nLet's play a country-capital game!")

countryCapital = [["Turkey","Ankara"],["Germany","Berlin"],["Egypt","Cairo"],["Australia","Canberra"],["Ireland","Dublin"],["Guyana","Georgetown"]]

from random import randint

choiceList = []

while True: # if the user wants to play again, enter into the loop again

    choice = randint(0, len(countryCapital)-1)

    if choice not in choiceList: # to check if the randomly picked number has been picked before

        choiceList.append(choice)

        enteredCapital = input(f"\nThis is country {len(choiceList)} out of {len(countryCapital)} countries. Please enter the capital of the country {countryCapital[choice][0]}: ")

        if enteredCapital == countryCapital[choice][1]:
            print("\nCongratulations, that is the Correct Answer!")

        else:
            print("\nSorry, that is an Incorrect Answer!")

        while True: # when input is not "y" or "n", ask the user to enter again until "y" or "n" is input

            option = ""

            if len(choiceList) != len(countryCapital):
                option = input("\nWould you like to play next country? (y/n): ")
            else:
                break

            if option.lower() != "y" and option.lower() != "n": # same as if option.lower() not in ["y", "n"]
                print("\nSorry, that is not a valid option! Please enter 'y' or 'n' only.")
                continue
            else:
                break

        if option.lower() == "n":
            print("\nYou have chosen not to play next country. Thank you for playing!")
            print("\nEnd of program.")
            break

        else:
            if len(choiceList) != len(countryCapital):
                print("\nYou have chosen to play next country. Please continue.")
            continue

    else:

        if len(choiceList) == len(countryCapital):
            while True:
                cont= input("\nYou have completed the country list. Do you want to play again? (y/n): ")
                if cont.lower() != "y" and cont.lower() != "n":
                    print("\nInvalid input. Please try again with 'y' or 'n' only.")
                    continue
                else:
                    break

            if cont.lower() == "y":
                choiceList = []
                continue
            if cont.lower() == "n":
                print("\nThank you for playing! Program ended..")
                break
        else:
            continue