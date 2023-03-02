import os
import subprocess

def add_user():
    print("Wlcome to adding user service!")

    confirm = "N"

    while confirm != "Y":
        username = input("Enter the name of the user: ")
        print("Do you want to add the user '" + username + "'? (Y/N)", end="")
        confirm = input().upper()
    os.system("sudo adduser " + username)


def remove_user():
    print("Wlcome to deleting user service!")

    confirm = "N"

    while confirm != "Y":
        username = input("Enter the name of the user: ")
        print("Do you want to add the user '" + username + "'? (Y/N)", end="")
        confirm = input().upper()
    subprocess.run(["sudo", "userdel", username])


def add_group():
    pass

def remove_group():
    pass


def show_grp_and_users():
    pass



def list_administration_options():
    print("""
        \n\nBelow listed the available commands. Enter one of the following(or 'q' to exit):
        \n\t - '1' to Add a user
        \n\t - '2' to remove a user
        \n\t - '3' to add a group
        \n\t - '4' to remove a group
        \n\t - '5' to show a group and its users
    """)


def ask_for_continuing():
    continueCheck = input("Do you want to use other commands? (Y/n)")
    return continueCheck.upper()


def main():

    print("Welcome to our program of linux administration!")

    while True:
        list_administration_options()

        choice = input("Choose from the list of commands above: ")

        if choice == "q":
            exitCheck = input("Do you want to exit (enter 'y' to exit)? ")
            if exitCheck == "y":
                break
        elif choice == "1":
            add_user()
            if ask_for_continuing() == "N":
                break
        elif choice == "2":
            remove_user()
            if ask_for_continuing() == "N":
                break
        elif choice == "3":
            add_group()
        elif choice == "4":
            remove_group()
        elif choice == "5":
            show_grp_and_users()
        else:
            print("Wrong choice! Please select one of the availble commands listed below!")
            continue



if __name__ == "__main__":
    main()

