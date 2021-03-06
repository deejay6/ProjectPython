# This contains all functions as a backend framework for spychat app
# Imports
from steganography.steganography import Steganography
from datetime import datetime


spy_credentials = {
    'username': ['admin'],
    'password': ['password'],
    'name': ['fSociety'],
    'spy rating': ['5'],
    'spy salutation': ['Mr.'],
    'spy status': ['Working !']
    }

friend_list = ['Trenton', 'Romero', 'Darlene', 'Elliot']


def add_friend():
    friend_added_username = raw_input("Enter username of your friend : ")
    if friend_added_username in spy_credentials['username']:
        x = spy_credentials['username'].index(friend_added_username)
        question = raw_input("Are you sure you want to add " + " " + spy_credentials['name'][x] + " ? (y/n)")
        if question is "y" or "Y":
            print "Adding..."
            friend_list.append(friend_added_username)
            print "Your new friend list : "
            print friend_list
            chat()
        else:
            print "friend not added."
            chat()
    else:
        question = raw_input("friend not found, try again ?(y/n)")
        if question is "y" or "Y":
            add_friend()
        else:
            print("going back to chat menu >")
            chat()


def remove_friend():
    print "Your current friends are > "
    print friend_list
    friend_remove_user = raw_input("Enter name of friend to be removed ")
    if friend_remove_user in friend_list:
        remove = friend_list.index(friend_remove_user)
        friend_list.pop(remove)
        print "Your friend list is now >"
        print friend_list
        question = raw_input("Remove more friends ? (y/n) ")
        if question is "Y" or "y":
            remove_friend()
        else:
            print "Moving back to chat menu >"
            chat()


def view_friends():
    print "This is your current friend list > "
    print friend_list
    question = raw_input("Would you like to edit friends ? (y/n) ")
    if question is "y" or "Y":
        ans = True
        while ans:
            print """
                        1.Add a friend
                        2.Remove a friend
                        3.Back
                        4.Exit
                        """
            ans = raw_input("What would you like to do ? ")
            if ans == "1":
                add_friend()
                ans = False
            if ans == "2":
                remove_friend()
                ans = False
            if ans == "3":
                chat()
                ans = False
            if ans == "4":
                exit()
            if ans != "":
                print "Invalid selection, try again"


def edit_profile_name():
    new_name = raw_input("Enter new name : ")
    edit_profile()

def edit_status():
    print "bla bla"
    edit_profile()


def edit_salutation():
    print "bla bla"
    edit_profile()


def edit_profile():
    ans = True
    while ans:
        print """
                1.Name
                2.Salutation
                3.Status
                4.Nothing at all/ Keep as it is...
                """
        ans = raw_input("What would you like to edit ? ")
        if ans == "1":
            edit_profile_name()
        if ans == "2":
            edit_salutation()
        if ans == "3":
            edit_status()
        if ans == "4":
            chat()
        if ans != "":
            "Invalid selection..."


def edit_profile_options():
    ans = True
    while ans:
        print """
                1.Edit profile options
                2.Back
                """
        ans = raw_input("Select an option : ")
        if ans == "1":
            edit_profile()
        if ans == "2":
            chat()
        if ans != "":
            print "invalid selection ...."


def chat():
    ans = True
    while ans:
        print """
            1.Send a message
            2.View messages
            3.View profile
            4.Edit Profile
            5.Set status
            6.view friend(s)
            7.Exit
            """
        ans = raw_input("What would you like to do? ")
        if ans == "1":
            print "Send message control line > "
            ans = False

        elif ans == "2":
            print "View message control line > "
            ans = False

        elif ans == "3":
            print "View profile control line >"
            ans = False

        elif ans == "4":
            print "Edit profile control line >"
            ans = False
            edit_profile()

        elif ans == "5":
            print "Set status control line >"
            ans = False

        elif ans == "6":
            print "View friend control line >"
            view_friends()
            ans = False

        elif ans == "7":
            print "Exiting"
            exit()

        elif ans != "":
            print "Not Valid Choice Try again"


def existing():
    spy_username = raw_input("Enter your username : ")
    spy_pass = raw_input("Enter password : ")
    if spy_username in spy_credentials['username']:
        x = spy_credentials['username'].index(spy_username)
        if spy_pass == spy_credentials['password'][x]:
            print "Welcome " + spy_username
            chat()
        else:
            print "Incorrect password... Exiting!"


def password():
    new_password = raw_input("Enter a password for your account ( 6 char min) : ")
    if len(new_password) < 6:
        print "password too short, try again..."
        password()
    else:
        print "password saved !"
        spy_credentials['password'].append(new_password)
        print "redirecting you to main page, login as existing user."
        main()


def new_user():
    new_username = str(raw_input("Enter a username for yourself (make it unique) : "))
    if new_username in spy_credentials['username']:
        print "username already exists.... try again "
        new_user()
    else:
        print "Adding username...."
        spy_credentials['username'].append(new_username)
        password()


def main():
    ans = True
    while ans:
        print """
        1.Existing user login
        2.New user
        3.Exit/Quit
        """
        ans = raw_input("What would you like to do? ")
        if ans == "1":
            print "Loading login form > "
            existing()
            ans = False

        elif ans == "2":
            print "Loading new user form > "
            new_user()
            ans = False

        elif ans == "3":
            print "Good bye mate..."
            exit()

        elif ans != "":
            print "Not Valid Choice Try again"

