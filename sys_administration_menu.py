#!/usr/bin/env python3

import os
import subprocess

def add_user():
    print("Wlcome to adding user service!")

    confirm = "N"

    while confirm != "Y":
        username = input("Enter the name of the user: ")
        print("Do you want to add the user '" + username + "'? (Y/N)", end="")
        confirm = input().upper()
    subprocess.run(["sudo", "adduser", username])


def remove_user():
    print("Wlcome to deleting user service!")

    confirm = "N"

    while confirm != "Y":
        username = input("Enter the name of the user: ")
        print("Do you want to remove the user '" + username + "'? (Y/N)", end="")
        confirm = input().upper()
    subprocess.run(["sudo", "userdel", username])

    # 

def add_group():
    print("Wlcome to adding group service!")

    confirm = "N"

    while confirm != "Y":
        groupname = input("Enter the name of the group: ")
        print("Do you want to add the group '" + groupname + "'? (Y/N)", end="")
        confirm = input().upper()
    subprocess.run(["sudo", "groupadd", groupname])

def remove_group():
    print("Wlcome to deleting group service!")

    confirm = "N"

    while confirm != "Y":
        groupname = input("Enter the name of the group: ")
        print("Do you want to delete the group '" + groupname + "'? (Y/N)", end="")
        confirm = input().upper()
    subprocess.run(["sudo", "groupdel", groupname])


def show_grp_and_users():
    print("Wlcome to listing groups and their users service!")

    
    groupname = input("Enter the name of the group: ")
    confirm = input().upper()
    os.system("sudo cat /etc/group | grep " + groupname)



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
            if ask_for_continuing() == "N":
                break
        elif choice == "4":
            remove_group()
            if ask_for_continuing() == "N":
                break
        elif choice == "5":
            show_grp_and_users()
            if ask_for_continuing() == "N":
                break
        else:
            print("Wrong choice! Please select one of the availble commands listed below!")
            continue



if __name__ == "__main__":
    main()



# //TODO: refacor functions into different files and import them