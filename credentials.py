import string
import random
import pyperclip
class Credential:
    """
    Class that generate new instances of user  credentials.
    """
    credential_list = [] 

    def save_credential(self):
        """
        function to save user details
        """

        Credential.credential_list.append(self)

    def delete_credential(self):
        """
        Function to remove user details
        """

        Credential.credential_list.remove(self)

    def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        """
        Generate password
        """
        generate_pass=''.join(random.choice(char) for _ in range(size))

        return generate_pass

    @classmethod
    def find_by_email(cls,number):
        """
        Method to search user by email
        """
        for credential in cls.credential_list:
            if credential.email == number:
                return credential

    @classmethod
    def credential_exist(cls,number):
        """
        Method to check if user exists
        """
        for credential in cls.credential_list:
            if credential.email == number:
                return True

    @classmethod
    def display_credential(cls):
        """
        Method to display user credentials
        """
        return cls.credential_list

    @classmethod
    def copy_email(cls,number):
        """
        class method to copy user email
        """
        credential_found = Credential.find_by_email(number)
        pyperclip.copy(credential_found.email)

    def __init__(self,email,platform,password):



        self.email = email
        self.platform = platform
        self.password = password 