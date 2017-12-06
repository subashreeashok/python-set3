'''
Name : Subashree
Setno: 3
Question_no:1
Description:
'''
def is_palindrome(str):
    print(str)
    f=str[0:5:2]
    print(f)
    if(str==str[::-1]):
        print "is palindrome"
    else:
        print "not palindrome"
str=raw_input("enter string: ")    
is_palindrome(str)
