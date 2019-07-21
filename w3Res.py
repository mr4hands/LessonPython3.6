#1

def count_chars(string):
    count = 0
    for char in string:
        count += 1
    return count

print(count_chars(input("enter a string")))


def count_per_char(string):
    thisdict = {}
    for char in string:
        if thisdict.get(char):
            thisdict[char] = thisdict.get(char) + 1
        else:
            thisdict[char] = 1
    print(thisdict)

count_per_char("ooossssd")

def create_a_string(string):
    print(string)
    string_size = str(string).__len__()
    print(string_size)
    if string_size >= 2:
        start = string[0:2]
        end = string[int(string_size)-2,int(string_size)]
        new_string = start+end
    else:
        new_string = ''
    print(new_string)
create_a_string("w3resource")
create_a_string("w3")
create_a_string("w")
