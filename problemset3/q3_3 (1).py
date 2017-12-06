'''
Name: subashree
setno:3
Qno:3
Description:to find e is in word or not
'''
def fn(w):
    #for i in w:
    if 'e' in w:
        print("false")
    elif 'E' in w:
        print("false")
    else:
        print("true")
w=raw_input("enter word:")
fn(w)

