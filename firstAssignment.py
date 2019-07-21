#A
#=========================
first = 7
second = 44.3
print(first + second) #51.3
print(first * second) #310.09999999999997
print(second / first) #6.328571428571428

#B
#========================
# a = 9, b = 8, c = 15
a = 8
a = 17
a = 9
b = 6
c = a+b
b = c+a
b = 8
print("a:",a,"b:",b,"c:",c)

#C
#=======================
# No, They are both strings

# the problem is with concating int. (TypeError: can only concatenate str (not "int") to str)
my_number = 5+5
print("result is:",my_number)

#D
#=======================
# the answer is 7
x = 5
y = 2.36
print(x+int(y))

#E
#=======================
x = 5
y = 1
if x > y:
    print("BIG")
if y > x:
    print("small")

#F
#=======================
var = 2
if var==1:
    print("summer")
elif var==2:
    print("winter")
elif var==3:
    print("fall")
elif var==4:
    print("spring")
else:
    print("Out of range")

#CHALLENGE
#=======================
#need to cast b to int
a = 8
b = "123"
print(a+int(b))


