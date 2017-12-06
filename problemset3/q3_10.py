'''
Name : Subahree
Setno: 3
Question_no:10 
'''
def is_anagram(x1,y1):
    length_x=len(x1)
    length_y=len(y1)
    if length_x==length_y:
        x1.sort()
        print(x1)
        y1.sort()
        print(y1)
        if x1==y1:
            print("true")
        else:
            print("false")
        print("len same")
    else:
        print("false")
x=raw_input("enter word1:")
y=raw_input("enter word2:")
x1=list(x)
y1=list(y)
#print(x1)
#print(y1)
is_anagram(x1,y1) 
