import secrets
import string

def main():
    print("Lets create a strong password!")

    length = input("Give password lenght (at least 10 characters): ")
    uppercase = input("Include uppercase letters?[y/n]")
    symbols = input("Include symbols? [y/n]:")

    alphabet = string.ascii_letters + string.digits #Characters that will be used
