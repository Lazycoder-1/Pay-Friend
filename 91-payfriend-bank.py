#
# # A bank app using Python
# # a user can create any type of account (savings or current account), name on the account , balance etc.
# # user can withdraw,deposit and check balance in the account
#
import random
main_account = []
def show_menu():
    print('Welcome To PayFriend Banking ')
    # print('Press HELP for assistance')
    # print('-------------------------')
def account_menu():
    user_input = input('What do you want to do [Create Account(C), Login(L)]: ')
    user_input = user_input.capitalize()

    if user_input == 'C':
        acc_name = input('Enter your name: ').capitalize()
        acc_type = input('What account do you want [Current Account(AC), Savings Account(SA)]; ').capitalize()
        acc_num = random.randint(10**17, 10**18 - 1)
        print('Hello {}'.format(acc_name))
    print('Your account number is {}'.format(acc_num))

show_menu()
account_menu()
