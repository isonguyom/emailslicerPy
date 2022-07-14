# Python Email Slicer
import re


print("WELCOME TO OUR EMAIL SLICER!!!")

is_running = True
def sliceEmail():
    # Remove spaces in the email address using the strip() method
    stripEmail = email.strip()

    # Slice the outcome around @ character
    username = stripEmail[:stripEmail.index("@")]
    domain = stripEmail[stripEmail.index("@") + 1:]

    # print the sliced email
    print("\n===================================")
    print("Your Username: ", username, "\nDomain name: ", domain)
    print("===================================\n")


while is_running:
    print("Email slicer is running...")
    # Allow user to enter an email address
    email = input("Please enter a valid email:\n")
    
    # Check for email validity
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(email_pattern, email)):
        sliceEmail()
    else:
        print("You entered an invalid email address")


    # Check wheather to terminate the loop
    try_again = input("Would you like to slice another email (y/n)? ")
    if try_again == "y":
        pass 
    
    if try_again == "n":
        print("Stopping email slicer... ")
        print("THANKS FOR USING OUR EMAIL SLICER!!!")
        is_running = False 
        # This is the same thing as a break.-  