'''
Name : Subashree
Setno: 3
Question_no:6
'''
def fn(wl,fr_l):
    count=0
    for i in fr_l:
        if i in wl:
            break
        else:
            count+=1
            print("count of words without forbidden:" +str(count))
            break
    if(count>0):        
      print("true") 
    if(count==0):
      print("false")
num=int(raw_input("enter range: "))
nw=int(raw_input("enter range for word:"))
wl=[]
for i in range(0,nw):
    w=raw_input("enter word:")
    wl.append(w)
fr_l=[]
for i in range(0,num):
    fr=raw_input("enter forbidden letters:")
    fr_l.append(fr)
    #print(fr_l)
fn(wl,fr_l)