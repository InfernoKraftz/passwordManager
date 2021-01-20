import random
import os

#Your password that will be asked everytime on login goes in the quotation marks.
masterPw = ""
password = input("Enter masterpassword: ")

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*!@#$%^&-_+=;:.>/?\|"

all = lower + upper + numbers + symbols
length = 16

while masterPw != password:
    if masterPw != password:
        print("Invalid password!")
        exit()
if masterPw == password:
    print("Welcome InfernoKraftz!")
def main():
    serviceChoice = input("(A)dd new password or (D)elete all passwords? (L)ist all Services or (Q)uit: ")
    userInput = "NVM"
    userPasswordChoice = ""
    if os.path.isfile('services.txt'):
        with open('services.txt', 'r') as f:
            servicesList = f.read()
            servicesList = servicesList.split(",")
    else:
        with open('services.txt','w') as f:
            pass
    if serviceChoice == "a":
        servicesList = []
        serviceName = input("Service name? ")
        while not userInput == "":
            password = "".join(random.sample(all, length))
            print(password)
            userInput = input("Press enter to confirm and press any key for another password choice: ")
            userPasswordChoice = password
            servicesList.append(serviceName + ":" + userPasswordChoice)
        with open('services.txt', 'a') as f:
            f.write(str(servicesList))
        main()
    elif serviceChoice == "A":
        servicesList = []
        serviceName = input("Service name? ")
        while not userInput == "":
            password = "".join(random.sample(all, length))
            print(password)
            userInput = input("Press enter to confirm and press any key for another password choice: ")
            userPasswordChoice = password
            servicesList.append(serviceName + ": " + userPasswordChoice + ", ")
        with open('services.txt', 'a') as f:
            f.append(str(servicesList))
        main()
    elif serviceChoice == "d":
        with open('services.txt', 'w') as f:
            f.write("")
        main()
    elif serviceChoice == "D":
        with open('services.txt', 'w') as f:
            f.write("")
        main()
    elif serviceChoice == "l":
        with open('services.txt', 'r') as f:
            print(f.read())
        main()
    elif serviceChoice == "L":
        with open('services.txt', 'r') as f:
            print(f.read())
        main()
    elif serviceChoice == "q":
        exit()
    elif serviceChoice == "Q":
        exit()
    else:
        print("Type a valid response, please!")
        main()
main()
