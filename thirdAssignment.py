from PIL import Image, ImageDraw

#########
# 1 + 2 #
#########

try:
    a = 1/0
except ZeroDivisionError as e:
    print('error:', e)


#########
#   3   #
#########

# yes, the code is legal

#########
#   4   #
#########
# All of the exception types (should be except with lowercase e)


#########
#   5   #
#########
# You want to catch specific exceptions and handle them differently

#########
#   6   #
#########
# except IOError catches exceptions caused by I/O operations
# except ZeroDivisionError catches exceptions the are raised when dividing by zero occurs

#########
#   7   #
#########
file_path = 'C:/Users/egilron/DevopsExperts/LessonPython3.6/resources/words.txt'

try:
    words_file = open(file_path,'w+',encoding='utf-8')


#########
#   8   #
#########

    words_file.write('Erez\n')
    words_file.close()
#########
#   9   #
#########
    words_file = open(file_path,'r',encoding='utf-8')
    content = words_file.read()
    print(content)
    words_file.close()

#########
#  10   #
#########
    words_file = open(file_path, 'a',encoding='utf-8')
    words_file.write('שם שלי באנגלית')
    words_file.close()
    words_file = open(file_path,'r', encoding='utf-8')
    content = words_file.read()
    print(content)
    words_file.close()

except IOError as e:
    print(e)

finally:
    print("this is the end my friend")

#===============#
#   CHALLENGE   #
#===============#

#installing pillow using pip
# adding the imports
try:
    image = Image.new('RGB',(100,50), color=(32,142,98))

    drawing = ImageDraw.Draw(image)
    drawing.text((10,10),"Hi Image", fill=(255,255,0))

    image.save('resources/my_new_image.jpeg')
except Exception as e:
    print(e)