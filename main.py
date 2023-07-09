import random
import string
from vault.database import Database
#Comment
def generate_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range (length))
    return password

def main():
    length = int(input("Enter desired length of the password: "))
    password = generate_password(length)
    print("Generated Password:", password)

    username = input("Enter the username: ")
    ip_address = input("Enter the IP address: ")
    domain_name = input("Enter the Domain name: ")
    
    db = Database()
    db.add_password(username, password, ip_address, domain_name)
    stored_password = db.get_password(username)

    if stored_password:
        print("Stored Password:", stored_password)
    else:
        print("Password Removed")

    username_to_remove = input("Enter the username to remove: ")
    db.remove_password(username_to_remove)
    print("Password removed.")

if __name__ == '__main__':
    main()


