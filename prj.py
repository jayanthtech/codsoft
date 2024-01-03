import random
import string

def generate_password(length):
    special_characters = "!@#$%&*"
    characters = string.ascii_letters + string.digits + special_characters
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator")
    length = int(input("Enter the desired length of the password: "))
    
    if length < 6:
        print("Password length should be at least 6 characters.")
    else:
        password = generate_password(length)
        print("Generated password: ", password)

if __name__ == "__main__":
    main()
