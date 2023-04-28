# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm he
# lp at https://www.jetbrains.com/help/pycharm/
# print("kwame")
#AES Cryptocraphy 

from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)
message = b"MSc. Information Technology-Group9"
encrypted_message = fernet.encrypt(message)
print("Your encrypted message is:", encrypted_message)
decrypted_message = fernet.decrypt(encrypted_message)
print("Your decrypted/plaintext is:", decrypted_message)




