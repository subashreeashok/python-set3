'''
Name: subashree
setno:3
Qno:4
Description:to find e is in word or not
'''
def fn(l):
    count=0
    length=len(l)
    print(length)
    for i in l:
        if 'e' in i:
            #print("false")
            break
        else:
            print("word without e: "+str(i))
            count+=1
    print(count) 
    percent=float((count)/float(length))*100
    print(percent)
n=int(raw_input("enter num: "))
l=[]
for i in range(0,n):
    w=raw_input("enter word: ")
    l.append(w)
    print(l)
fn(l)
