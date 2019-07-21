# import array
#
# ###############
# #A
# ###############
# X = 2
# Y = 4
# if X > Y:
#     print("BIG")
# elif X < Y:
#     print("small")
#
#
# ##############
# #B
# ##############
# for x in range(5):
#     print(x)
#
#
# ##############
# #C
# ##############
# season = 3
# if season == 1:
#     print("summer")
# elif season == 2:
#     print("winter")
# elif season == 3:
#     print("fall")
# elif season == 4:
#     print("spring")
#
#
# #############
# #D
# #############
# #1) the loop will run 10 times
# #2) the number 10 will be printed last
#
# #############
# #E
# #############
# age = 36
# first_letter_of_last_name = 'g'
# shekel_to_dollar_rate = 3.61
# i_flew_abroad = True
# appartment_number = 3
#
# print(age, first_letter_of_last_name, shekel_to_dollar_rate, i_flew_abroad, appartment_number)
# print(age + shekel_to_dollar_rate)
#
# #############
# #F
# #############
# phone_number = input('type your phone number:')
# print("phone number {0}".format(phone_number))
#
# #############
# #G
# #############
# def printHello():
#     print('hello')
#
#
# def calculate():
#     print(5+2.3)
#
# #############
# #H
# #############
# def print_name(name):
#     print(name)
#
#
# def divide_by_two(number):
#     print(number / 2)
#
# ##############
# #I
# ##############
# def return_sum(num_a, num_b):
#     return num_a + num_b
#
#
# def spaced_string(string_a, string_b):
#     string_c = "{0} {1}".format(string_a, string_b)
#     return string_c
#
#
# ###############
# #J
# ###############
# my_array = array.array('i',[2,3,5])
# for item in my_array:
#     print(item)
#
# ##################
# ### CHALLENGES ###
# ##################
#
# ##################
# #K
# ##################
# for i in range(6):
#     for j in range(i):
#         print('*',end='')
#     print('')
#
#
# ##################
#L
##################
startpoint = 0
endpoint = 6
for i in range(7):
    for j in range(7):
        if j == startpoint or j == endpoint:
            print('*', end='')
        else:
            print(' ',end='')
    print('')
    startpoint += 1
    endpoint -= 1