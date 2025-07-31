import secrets
import string

def main():
    print("Lets create a strong password!")
    while True:
        length_input = input("Give password length (at least 15 characters): ")
        try:
            length = int(length_input)
            if length >= 15:
                break
            else:
                print("Password length must be at least 15 characters. Try again.")
        except ValueError:
            print("Please enter a valid number (digits only).")

    uppercase_input = input("Include uppercase letters?[y/n]")
    lowercase = string.ascii_lowercase

    symbols_input = input("Include symbols? [y/n]:")
    symbols = '-_*&^%$#@!'

    alphabet = lowercase + string.digits #Characters that will be used (only lowercase at the beggining)
        
    if(uppercase_input == "y"):
        uppercase = string.ascii_uppercase
        alphabet += uppercase
        if(symbols_input == "y"):
            alphabet += symbols #append symbols if the user wants to
            password = ''.join(secrets.choice(alphabet) for i in range(length))
            print(password)
        else:
           password = ''.join(secrets.choice(alphabet) for i in range(length))
           print(password)
    else:
        if(symbols_input == "y"):
            alphabet += symbols #append symbols if the user wants to
            password = ''.join(secrets.choice(alphabet) for i in range(length))
            print(password)
        else:
            password = ''.join(secrets.choice(alphabet) for i in range(length))
            print(password)


main()