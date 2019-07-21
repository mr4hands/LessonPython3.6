#########
#1
#########
a = 1
for a in range(11):
    print(a)


#########
#2
#########
user_num = int(input("please enter a number:"))
if user_num % 2:
    print('-')
else:
    print('+')


#########
#3
#########
num_a = int(input("please enter a number"))
num_b = int(input("please enter another number"))

def compare(a,b):
    if a>b:
        return a
    elif a<b:
        return b
    else:
        return "the numbers are equal"

print(compare(num_a,num_b))


#########
#4
#########
age = int(input("enter your age"))
height = int(input("enter your height"))

if age > 10 and height > 120:
    print("Welcome to the rollercoaster")
else:
    print("Sorry.. maybe next time")


#########
#5
#########
num_a = int(input("enter number"))
num_b = int(input("enter another one"))

def check_if_equal(a, b):
    if a == b:
        return "equal"
    else:
        return "not equal"

print(check_if_equal(num_b,num_a))

#########
#6
#########

#the biggest concern with loops is infinite itirations and complexity

#########
#7
#########

def get_name(name):
    print("Your name is ", name)

get_name(input("please enter your name:"))

########
#8
########

number = int(input("enter a number"))
print( number > 100 )