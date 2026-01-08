import csv
username = []


with open("accounts.txt","r") as file:
    csvReader = csv.reader(file, delimiter=",")
    for field in csvReader:

        username.append(field[0].strip().lower())

    print(f"Original order is {username}.")

    i = 1
    while i < len(username):
        j = 0
        while j < i:
            if username[i-j] > username[i-j-1]:

                break
            else:
                transit = username[i-j-1]
                username[i-j-1] = username[i-j]
                username[i-j] = transit
                j = j+1
        i = i+1
print(f"New order is {username}.")