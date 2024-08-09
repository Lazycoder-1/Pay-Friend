
# A bank app using Python
# a user can create any type of account (savings or current account), name on the account , balance etc.
# user can withdraw,deposit and check balance in the account


# import random
# print('Welcome To PayFriend Banking ')
#
# user_input = input('What do you want to do [Create Account(C),Login(L)]: ').capitalize()
# if user_input == 'C':
#     acc_name_new = input('Enter your name: ').capitalize()
#     acc_type = input('What account do you want [Current Account(AC), Savings Account(SA)]; ').capitalize()
#     acc_num_new = random.randint(10 ** 17, 10 ** 18 - 1)
#     print('Hello {}'.format(acc_name_new))
#     print('Your new account has been created')
#     print('Your account number is {}'.format(acc_num_new))
#
#     print('CONGRATULATIONS YOUR ACCOUNT HAS BEEN SUCCESSFULLY CREATED')
#     print('----- WHAT DO YOU WANT TO DO NEXT -----')
#     print('Press ADD FUNDS to add funds to your account')
#     print('Press WITHDRAW to withdraw funds from your account')
#     print('Press VIEW to view your account balance')
#     print('Press HELP for assistance')
#     print('-------------------------')
#     user_amount_new = 0
#     while True:
#         acc_new = input('> ')
#         if acc_new == 'ADD FUNDS':
#             user_amount_n = input('Enter amount you want to add: ')
#             user_amount_new += int(user_amount_n)
#             print('You have deposited {}$ in your account'.format(user_amount_new))
#         elif acc_new == 'WITHDRAW':
#             user_withdraw_new = int(input('Enter amount you want to withdraw: '))
#             if user_withdraw_new > user_amount_new:
#                 print('You have insufficient funds in your account')
#             else:
#                 user_amount_new -= user_withdraw_new
#                 print('You have withdrawn {}$. Your remaining balance is {}$'.format(user_withdraw_new, user_amount_new))
#         elif acc_new == 'VIEW':
#             user_amount_new = user_amount_new
#             print('Here is your account info, you have {}$ in your account'.format(user_amount_new))
#             break
#
# else:
#     user_name = input('Enter your username: ').capitalize()
#     user_password = input('Enter your password: ')
#     print('Hello {}, Welcome To PayFriend Banking'.format(user_name))
#     print('----- WHAT DO YOU WANT TO DO NEXT ----')
#     print('Press ADD FUNDS to add funds to your account')
#     print('Press WITHDRAW to withdraw funds from your account')
#     print('Press VIEW to view your account balance')
#     print('Press HELP for assistance')
#     print('-------------------------')
#     user_amount_l = 0
#     while True:
#         acc_user_l = input('> ')
#         if acc_user_l == 'ADD FUNDS':
#             user_amount = input('Enter amount you want to add: ')
#             user_amount_l += int(user_amount)
#             print('You have deposited {}$ in your account'.format(user_amount_l))
#             print('Your new balance is {}$'.format(user_amount_l))
#         elif acc_user_l == 'WITHDRAW':
#             user_withdraw_l = int(input('Enter amount you want to withdraw: '))
#             if user_withdraw_l > user_amount_l:
#                 print('You have insufficient funds in your account')
#             else:
#                 user_amount_l -= user_withdraw_l
#                 print('You have withdrawn {}$. Your remaining balance is {}$'.format(user_withdraw_l, user_amount_l))
#         elif acc_user_l == 'VIEW':
#             user_amount_l = user_amount_l
#             print('Here is your account info, you have {}$ in your account'.format(user_amount_l))

# Improved version from ChatGPT
import random
def create_account():
    acc_name_new = input('Enter your name: ').capitalize()
    acc_type = input('What account do you want [Current Account(CA), Savings Account(SA)]: ').capitalize()
    acc_num_new = random.randint(10 ** 17, 10 ** 18 - 1)

    print(f'Hello {acc_name_new}')
    print('Your new account has been created')
    print(f'Your account number is {acc_num_new}')
    print('CONGRATULATIONS, YOUR ACCOUNT HAS BEEN SUCCESSFULLY CREATED')

    return acc_name_new, acc_num_new, 0
def banking_menu(user_name):
    print(f'Hello {user_name}, Welcome To PayFriend Banking')
    print('----- WHAT DO YOU WANT TO DO NEXT -----')
    print('Press ADD FUNDS to add funds to your account')
    print('Press WITHDRAW to withdraw funds from your account')
    print('Press VIEW to view your account balance')
    print('Press HELP for assistance')
    print('Press EXIT to log out')
    print('-------------------------')
def account_actions(user_amount):
    while True:
        acc_action = input('> ').upper()

        if acc_action == 'ADD FUNDS':
            user_amount_n = input('Enter amount you want to add: ')
            user_amount += int(user_amount_n)
            print(f'You have deposited {user_amount_n}$ in your account.')
            print(f'Your new balance is {user_amount}$')

        elif acc_action == 'WITHDRAW':
            user_withdraw_new = int(input('Enter amount you want to withdraw: '))
            if user_withdraw_new > user_amount:
                print('You have insufficient funds in your account.')
            else:
                user_amount -= user_withdraw_new
                print(f'You have withdrawn {user_withdraw_new}$. Your remaining balance is {user_amount}$.')

        elif acc_action == 'VIEW':
            print(f'Here is your account info, you have {user_amount}$ in your account.')

        elif acc_action == 'HELP':
            print('For assistance, please visit our website or contact customer support.')

        elif acc_action == 'EXIT':
            print('Logging out...')
            break

        else:
            print('Invalid option, please try again.')

    return user_amount
def main():
    print('Welcome To PayFriend Banking')

    while True:
        user_input = input('What do you want to do [Create Account(C), Login(L)]: ').capitalize()

        if user_input == 'C':
            user_name, acc_num, user_amount = create_account()
        else:
            user_name = input('Enter your username: ').capitalize()
            _ = input('Enter your password: ')  # Simulate password entry
            user_amount = 0  # Simulate existing balance retrieval

        banking_menu(user_name)
        user_amount = account_actions(user_amount)

        # Ask if the user wants to run the program again
        restart = input('Do you want to perform another action? (yes/no): ').lower()
        if restart != 'yes':
            print('Thank you for using PayFriend Banking. Goodbye!')
            break

if __name__ == "__main__":
    main()



