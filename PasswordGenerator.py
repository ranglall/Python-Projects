import random
import string

"""
PasswordGenerator.py
Author: Breanna Ranglall
User inputs password requirements and code outputs appropiate password
"""

#Asks the user if they want a generated password
def main():
    startGenerator = input("Do you want a generated password? Yes or No: ")

    if startGenerator.lower() == "yes":  #Convert input to lowercase to handle different cases
        password_rules()  #Call the passwordRules function
    else:
        print("Ok, have a nice day!")

#Gathers rules for the password
def password_rules():

    #Ask for minimum length
    minLength = int(input("Enter minimum character length for your password: "))

    #Ask if they need an uppercase letter
    uppercase = get_boolean_input("Do you need at least one uppercase letter? Yes or No: ")

    #Ask if they need a number
    number = get_boolean_input("Do you need at least one number? Yes or No: ")

    #Ask if they need a speacial character
    specialCharacter = get_boolean_input("Do you need at least one special character? Yes or No: ")

    #Calls function to generate password and prints it
    generated_password = generate_password(minLength, uppercase, number, specialCharacter)
    print()
    print("Your generated password is:", generated_password)

#Asks for appropiate boolean input until one is given
def get_boolean_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lower() == "yes":
            return True
        elif user_input.lower() == "no":
            return False
        else:
            print("Please enter 'Yes' or 'No'.")

#Generates a password based on requirements
def generate_password(minLength, uppercase, number, specialCharacter):
    characters = string.ascii_letters
    if uppercase:
        characters += string.ascii_uppercase
    if number:
        characters += string.digits
    if specialCharacter:
        characters += string.punctuation

    # Generate the password of the given minimum length
    password = ''.join(random.choice(characters) for _ in range(minLength))
    return password
    
main()
