from user import User
from credentials import Credential

def create_user(firstname,lastname,phone,email,password):

    new_user = User(firstname,lastname,phone,email,password)
    return new_user

def create_credential(email,platform,password):

    new_credential =  Credential(email,platform,password)
    return new_credential

def generate_password():
    
    gen_pass = Credential.generate_password()
    return gen_pass

def save_users(user):

    user.save_user()

def save_credential(credential):

    credential.save_credential()

def del_user(user):

    user.delete_user()

def delete_credential(credential):

    credential.delete_credential()

def find_user(number):

    return User.find_by_number(number)

def find_credential(number):

    return Credential.find_by_email(number)

def check_existing_users(number):

    return User.user_exist(number)

def check_existing_credential(number):

    return Credential.credential_exist(number)

def display_users():

    return User.display_users()

def display_credential():

    return Credential.display_credential()

def test_copy_email():

    return User.copy_email()

def test_copy_email():

    return Credential.copy_email()


def main():

    print("hello.What is your name?")

    user_name = input()

    print(f"so {user_name}. What would you like to do")

    print('\n')

    while True:

        print("Use these short codes :")
        print("CU - Create a New User")
        print("DU - Display Users")
        print("FU - Find a User")
        print("CA - Create An Account")
        print("DI - Display Account Information")
        print("DA - Delete Account")
        print("EX - Exit")


        short_code = input().lower()

        if short_code == 'cu':

            print("New User")
            print("-"*10)

            print ("First name .....")
            f_name = input()

            print("Last name ....")
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()

            print("Password .....")
            e_pass = input()

            save_users(create_user(f_name,l_name,p_number,e_address,e_pass))

            print('\n')

            print(f"New User {f_name} {l_name} created")

            print ('\n')

        elif short_code == 'dis':
            if display_users():

                print("Here are our users")

                print('\n')

                for user in display_users():
                    print(f"{user.first_name} {user.last_name} .....{user.phone_number}")

                print('\n')

            else:

                print('\n')

                print("You dont seem to have any users saved yet")

                print('\n')

        elif short_code == 'fu':

            print("Enter the number you want to search for")

            search_number = input()

            if check_existing_users(search_number):

                search_user = find_user(search_number)

                print(f"{search_user.first_name} {search_user.last_name}")

                print('-' *20)

                print(f"Phone number...........{search_user.phone_number}")

                print(f"Email address .........{search_user.email}")

            else:

                print("User does not exist")


        elif short_code == 'da':

            if display_credential():
                print("Here is a list of all your credentials")

                print('\n')

                for credential in display_credential():

                        print(f"{credential.email} {credential.platform} .....{credential.password}")
                        print('\n')

            else:

                print('\n')

                print("You don't have any credentials")

                print('\n')

        elif short_code == "de":

            print("Starting to delete .......")
            print("Enter Email .......")
            del_name = input(" ")

            delete_credential(del_name)

        elif short_code == "ex":

            print("ADIOS!")

            break

        else:

            print("Please use the short codes")


if __name__ == '__main__':

    main()