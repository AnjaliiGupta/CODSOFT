#---------------------------------------PasswordGenerator------------------------------------
import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="!@#$%^&*()_."

string=lower+upper+numbers+symbols


#Prompt the user for the password length
password_length=int(input("Enter the desired password length:"))
password=""


#Generate and display the password
for a in range(password_length):
    password+=random.choice(string)
print("Your password is:",password)