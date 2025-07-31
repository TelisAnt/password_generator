import secrets
import string
import math

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

    while True:
        uppercase_input = input("Include uppercase letters?[y/n]")
        try:
            if (uppercase_input == "y") or (uppercase_input =="n"):
                break
            else:
                print("Include uppercase letters?[y/n]. Try again.")
        except ValueError:
            print("Please enter a valid answer (y/n only).")

    lowercase = string.ascii_lowercase

    symbols_input = input("Include symbols? [y/n]:")

    while True:
        symbols_input = input("Include symbols? [y/n]:")
        try:
            if (symbols_input == "y") or (symbols_input =="n"):
                break
            else:
                print("Include symbols?[y/n]. Try again.")
        except ValueError:
            print("Please enter a valid answer (y/n only).")
            
    symbols = '-_*&^%$#@!'

    alphabet = lowercase + string.digits #Characters that will be used (only lowercase at the beggining)
        
    if(uppercase_input == "y"):
        uppercase = string.ascii_uppercase
        alphabet += uppercase
        if(symbols_input == "y"):
            alphabet += symbols #append symbols if the user wants to
            password = ''.join(secrets.choice(alphabet) for i in range(length))
            entropy = math.log2(len(alphabet)) * length  #Calculating entropy
            print("Password:", password)
            print("Entropy: ", entropy)
            print(f"Strength: {'Weak' if entropy < 60 else 'Good' if entropy < 80 else 'Strong'}")
        else:
           password = ''.join(secrets.choice(alphabet) for i in range(length))
           print("Password:", password)
           entropy = math.log2(len(alphabet)) * length
           print("Entropy: ", entropy)
           print(f"Strength: {'Weak' if entropy < 60 else 'Good' if entropy < 80 else 'Strong'}")
    else:
        if(symbols_input == "y"):
            alphabet += symbols #append symbols if the user wants to
            password = ''.join(secrets.choice(alphabet) for i in range(length))
            print("Password:", password)

            entropy = math.log2(len(alphabet)) * length
            print("Entropy: ", entropy)
            print(f"Strength: {'Weak' if entropy < 60 else 'Good' if entropy < 80 else 'Strong'}")
        else:
            password = ''.join(secrets.choice(alphabet) for i in range(length))
            print("Password:", password)
            entropy = math.log2(len(alphabet)) * length 
            print("Entropy: ", entropy)
            print(f"Strength: {'Weak' if entropy < 60 else 'Good' if entropy < 80 else 'Strong'}")


main()