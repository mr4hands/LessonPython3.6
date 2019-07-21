import datetime
import sys
print('''
#===============================
#1
#===============================
''')
name = input("Enter your name:")
print("hello")
print(name)
print('''
#===============================
#2
#===============================
''')
x = input("enter a number:")
y = input("enter another number:")
print("the sum of the numbers is:", int(x)+int(y))
print('''
#===============================
#3
#===============================
''')
version = sys.version
print("the python version is:",version)
print('''
#===============================
#4
#===============================
''')
word = input("enter a word:")
last_char_pos = word.__len__() - 1
reverse = ''
for i in range(word.__len__()):
    reverse += word[last_char_pos-i]
print("reverse word is:",reverse)
print('''
#===============================
#5
#===============================
''')
word = input("enter a word:")
print("total letters in the word is:",word.__len__())
print('''
#===============================
#6
#===============================
''')
now = datetime.datetime.now()
print("the current date and time is:", str(now))
print('''
#===============================
#7
#===============================
''')
a = int(input("enter a number:"))
b = int(input("enter another number:"))
if a > b :
    bigger = a
elif b > a:
     bigger = b
else:
     bigger = "the numbers are equal."
print("the bigger number is:", bigger)
print('''
#===============================
#8
#===============================
''')
print("x = 120")
x = 120
if (x > 5 and x < 200):
    print("MATCH")
