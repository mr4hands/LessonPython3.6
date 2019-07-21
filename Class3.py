try:
    my_file = open('C:\\Useaaars\\egilron\\DevopsExperts\\LessonPython3.6\\resources\\text.txt','r', encoding='utf-8')
    content = my_file.read()
    my_file.close()
    print(content)
except IOError as e:
    print("failed openning the file with following error:")
    print(e)
finally:
    print('suddenlyyy!!!!')
my_file = open('C:\\Users\\egilron\\DevopsExperts\\LessonPython3.6\\resources\\text.txt','a')
my_file.write("now for something completely different")
my_file.close()
print('finished the run')


