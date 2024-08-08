#
# # A bank app using Python
# # a user can create any type of account (savings or current account), name on the account , balance etc.
# # user can withdraw,deposit and check balance in the account
#
import random
print('Welcome To PayFriend Banking ')

user_input = input('What do you want to do [Create Account(C),Login(L)]: ').capitalize()
if user_input == 'C':
    acc_name_new = input('Enter your name: ').capitalize()
    acc_type = input('What account do you want [Current Account(AC), Savings Account(SA)]; ').capitalize()
    acc_num_new = random.randint(10 ** 17, 10 ** 18 - 1)
    print('Hello {}'.format(acc_name_new))
    print('Your account number is {}'.format(acc_num_new))

    print('CONGRATULATIONS YOUR ACCOUNT HAS BEEN SUCCESSFULLY CREATED')
    print('----- WHAT DO YOU WANT TO DO NEXT ----')
    print('Press ADD FUNDS to add funds to your account')
    print('Press WITHDRAW to withdraw funds from your account')
    print('Press VIEW to view your account balance')
    print('Press HELP for assistance')
    print('-------------------------')
    user_amount_new = 0
    while True:
        acc_new = input('> ')
        if acc_new == 'ADD FUNDS':
            user_amount_n = input('Enter amount you want to add: ')
            user_amount_new += int(user_amount_n)
            print('You have deposited {} in your account'.format(user_amount_new))
        elif acc_new == 'WITHDRAW':
            user_withdraw_new = int(input('Enter amount you want to withdraw: '))
            if user_withdraw_new > user_amount_new:
                print('You have insufficient funds in your account')
            else:
                user_amount_new -= user_withdraw_new
                print('You have withdrawn {}. Your remaining balance is {}'.format(user_withdraw_new, user_amount_new))
        elif acc_new == 'VIEW':
            user_amount_new = user_amount_new
            print('Here is your account info, you have {} in your account'.format(user_amount_new))
            break

else:
    print('----- WHAT DO YOU WANT TO DO NEXT ----')
    print('Press ADD FUNDS to add funds to your account')
    print('Press WITHDRAW to withdraw funds from your account')
    print('Press VIEW to view your account balance')
    print('Press HELP for assistance')
    print('-------------------------')
    user_amount_l = 0
    while True:
        acc_user_l = input('> ')
        if acc_user_l == 'ADD FUNDS':
            user_amount = input('Enter amount you want to add: ')
            user_amount_l += int(user_amount)
            print('You have deposited {} in your account'.format(user_amount_l))
            print('Your new balance is {}'.format(user_amount_l))
        elif acc_user_l == 'WITHDRAW':
            user_withdraw_l = int(input('Enter amount you want to withdraw: '))
            if user_withdraw_l > user_amount_l:
                print('You have insufficient funds in your account')
            else:
                user_amount_l -= user_withdraw_l
                print('You have withdrawn {}. Your remaining balance is {}'.format(user_withdraw_l, user_amount_l))
        elif acc_user_l == 'VIEW':
            user_amount_l = user_amount_l
            print('Here is your account info, you have {} in your account'.format(user_amount_l))

















# def account_menu_new():
#     user_input = input('What do you want to do [Create Account(C), Login(L)]: ')
#     user_input = user_input.capitalize()
#
#     if user_input == 'C':
#         acc_name = input('Enter your name: ').capitalize()
#         acc_type = input('What account do you want [Current Account(AC), Savings Account(SA)]; ').capitalize()
#         acc_num = random.randint(10**17, 10**18 - 1)
#         print('Hello {}'.format(acc_name))
#         print('Your account number is {}'.format(acc_num))
#
#         print('Press ADD FUNDS to add funds to your account')
#         print('Press WITHDRAW to withdraw funds from your account')
#         print('Press VIEW to view your account balance')
#         print('Press HELP for assistance')
#         print('-------------------------')
#
# def account_menu_log():
#     if user_input == 'L':
#         acc_name = input('Enter your name: ').capitalize()
#         acc_num2 = input('Enter your account number: ')
#         print('Hello {}'.format(acc_name))
#         print('Press ADD FUNDS to add funds to your account')
#         print('Press WITHDRAW to withdraw funds from your account')
#         print('Press VIEW to view your account balance')
#         print('Press HELP for assistance')
#         print('-------------------------')
#
#     user_amount_init = 0
#     while True:
#         acc_user = input('> ')
#         if acc_user == 'ADD FUNDS':
#             user_amount = input('Enter amount you want to add: ')
#             user_amount_init += int(user_amount)
#             print('You have deposited {} in your account'.format(user_amount))
#             print('Your new balance is {}'.format(user_amount_init))
#         elif acc_user == 'WITHDRAW':
#             user_withdraw = int(input('Enter amount you want to withdraw: '))
#             if user_withdraw > user_amount_init:
#                 print('You have insufficient funds in your account')
#             else:
#                 user_amount_init -= user_withdraw
#                 print('You have withdrawn {}. Your remaining balance is {}'.format(user_withdraw, user_amount_init))
#         elif acc_user == 'VIEW':
#             user_amount_init = user_amount_init
#             print('Here is your account info, you have {} in your account'.format(user_amount_init))
#
# show_menu()
# account_menu_new()
# account_menu_log()

