'''
Name : Subashree
Setno: 3
Question_no:7
Description:check whether word is in string of letters
'''


def using_only(word,string):
    for i in word:
        if i not in string:
            return "false"
    return "true"        
            
word=raw_input("enter word: ")
string=list(raw_input("enter string of letters: "))
a=using_only(word,string)
print(a)