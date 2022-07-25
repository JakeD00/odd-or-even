import os

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
    os.system('pause')
else:
    print("This is an odd number.")
    os.system('pause')