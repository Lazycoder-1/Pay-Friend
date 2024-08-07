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
    elif user_input == 'L':
        acc_name = input('Enter your name: ').capitalize()
        acc_num2 = input('Enter your account number: ')
        print('Hello {}'.format(acc_name))
        print('Press ADD FUNDS to add funds to your account')
        print('Press WITHDRAW to withdraw funds from your account')
        print('Press VIEW to view your account balance')
        print('Press HELP for assistance')
        print('-------------------------')

    user_amount_init = 0
    while True:
        acc_user = input('> ')
        if acc_user == 'ADD FUNDS':
            user_amount = input('Enter amount you want to add: ')
            user_amount_init += int(user_amount)
            print('You have deposited {} in your account'.format(user_amount))
            print('Your new balance is {}'.format(user_amount_init))
        elif acc_user == 'WITHDRAW':
            user_withdraw = int(input('Enter amount you want to withdraw: '))
            if user_withdraw > user_amount_init:
                print('You have insufficient funds in your account')
            else:
                user_amount_init -= user_withdraw
                print('You have withdrawn {}. Your remaining balance is {}'.format(user_withdraw, user_amount_init))
        elif acc_user == 'VIEW':
            user_amount_init = user_amount_init
            print('Here is your account info, you have {} in your account'.format(user_amount_init))


# def main():
#     print('Press ADD FUNDS to add funds to your account')
#     print('Press WITHDRAW to withdraw funds from your account')
#     print('Press VIEW to view your account balance')
#     print('Press HELP for assistance')
#     print('-------------------------')




show_menu()
account_menu()
