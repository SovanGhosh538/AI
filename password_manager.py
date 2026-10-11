import random
import string

password = {}

try:
    with open("password.txt","r") as file:
        for line in file:
            website, pas = line.strip().split(":")
            password[website] = pas

except:
    pass

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%&"
    password = "".join(random.choice(chars) for _ in range(8))
    return password

while True:
    print("----PERSONAL PASSWORD MANAGER----")
    print("1.Save password")
    print("2.View password")
    print("3.Generate password")
    print("4.Exit")
    choice = input("enter your choice: ")

    if choice == '1':
        site = input("Enter website: ")
        pas = input("Enter password: ")

        password[site] = pas

        with open("password.txt","a") as file:
            file.write(f"{site}:{pas}\n")

        print("Saved!")

    elif choice == '2':
        if not password:
            print("No data!")
        else:
            for site, pas in password.items():
                print(site,":",pas)

    elif choice == '3':
        print("Generated Password: ",generate_password())

    elif choice == '4':
        print("Exiting....")
        break

    else:
        print("Invalid Input!")