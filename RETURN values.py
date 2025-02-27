def reverse_string (fstring):
    bstring =""
    for i in fstring:
        bstring = i + bstring
    return bstring

name =  input("Enter your name: ")
print(reverse_string(name))