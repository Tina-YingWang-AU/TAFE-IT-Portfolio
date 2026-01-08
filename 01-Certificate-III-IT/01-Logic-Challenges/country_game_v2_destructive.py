# Program for Country-Capital matching Game
# first randomly pick one country, then remove it from the country list. Then randomly pick another country from the remaining country list. So on and on. During the process, ask the user if they want to play next country, if not, program ends.
# When all the countries in the list have been picked once, ask the user if they want to play the list again, if not, program ends.

print("\nLet's play a country-capital game!")

originalCountryCapital = [["Turkey","Ankara"],["Germany","Berlin"],["Egypt","Cairo"],["Australia","Canberra"],["Ireland","Dublin"],["Guyana","Georgetown"]]

tempCountryCapital = [["Turkey","Ankara"],["Germany","Berlin"],["Egypt","Cairo"],["Australia","Canberra"],["Ireland","Dublin"],["Guyana","Georgetown"]]

from random import randint
import copy # in order to use deepcopy

cont = ""

while True:
    for i in range(len(originalCountryCapital)):

        choice = randint(0,len(tempCountryCapital)-1)

        enteredCapital = input(f"\nWhat is the capital of {tempCountryCapital[choice][0]}? ({i + 1} in {len(originalCountryCapital)} countries) Your answer is: ")

        if enteredCapital.lower() == tempCountryCapital[choice][1].lower():

            print("\nYour answer is correct.")

        else:
            print("\nYour answer is incorrect.")

        del tempCountryCapital[choice]

        while True:
            if tempCountryCapital != []:

                cont = input("\nWould you like to play next country? (y/n): ")

                if cont.lower() != "y" and cont.lower() != "n":
                    print("\nInvalid input. Please try again with only 'y' or 'n'.")
                    continue
                else:
                    break
            else:
                break

        if cont.lower() == "n":
            break

    if cont.lower() == "n":
        print("\nYou chose not to play next country. Thank you for playing. Program ended..")
        break

    if tempCountryCapital == []:
        while True:
            option = input("\nThe country list is completed. Would you like to play again? (y/n): ")
            if option.lower() != "y" and option.lower() != "n":
                print("\nInvalid input. Please try again with only 'y' or 'n'.")
                continue
            else:
                break

        if option.lower() == "n":
            print("\nYou chose not to play the list again. Thank you for playing. Program ended..")
            break
        else:
            tempCountryCapital = copy.deepcopy(originalCountryCapital) # needs to use deep copy here. If just use shallow copy (meaning, just use =) originalCountryCapital list would change the same as tempCountryCapital.
            print("\nYou chose to play the list again.")
            continue
