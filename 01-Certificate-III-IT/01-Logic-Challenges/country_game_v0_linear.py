# Program for Country-Capital matching Game

countryCapital = [["Turkey","Ankara"],["Germany","Berlin"],["Egypt","Cairo"],["Australia","Canberra"],["Ireland","Dublin"],["Guyana","Georgetown"]]

print("\nLet's play a country-capital game!")



while True:

    score = 0

    for i in range(len(countryCapital)):

        enteredCapital = input(f"\nPlease enter the capital of the country {countryCapital[i][0]} ({i + 1} of {len(countryCapital)} countries): ")

        if enteredCapital == countryCapital[i][1]:
            print("\nCongratulations, that is the Correct Answer!")
            if i < len(countryCapital) - 1:
                print("\nNow continue our game with the next country!")
            score = score + 1

        else:
            print("\nSorry, that is an Incorrect Answer!")
            if i < len(countryCapital) - 1:
                print("\nNow continue our game with the next country!")

        if i == len(countryCapital) - 1:
            print("\nThis is the end of the country list!")
            print(f"\nYour score for this round is: {score/len(countryCapital)*100:.2f}%.")




    while True:
        option = input("\nWould you like to play again? (y/n): ")

        if option.lower() != "y" and option.lower() != "n": # same as if option.lower() not in ["y", "n"]
            print("\nSorry, that is not a valid option! Please enter 'y' or 'n' only.")
            continue
        else:
            break

    if option.lower() == "n":
        print("\nYou have chosen not to play again. Thank you for playing!")
        print("\nEnd of program.")
        break
    else:
        print("\nYou have chosen to play again. Please continue.")
        continue