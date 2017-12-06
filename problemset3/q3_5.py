'''
Name : Subashree
Setno: 3
Question_no:5
'''

def fn(w,fr_l):
    count=0
    for i in fr_l:
        if i in w:
            break
        else:
            count+=1
    #print(count)
    if(count>0):        
      print("true") 
    if(count==0):
      print("false")
num=int(raw_input("enter range: "))
w=raw_input("enter word:")
#storing forbidden letters in list
fr_l=[]
#to get many forbidden letters 
for i in range(0,num):
    fr=raw_input("enter forbidden letters:")
    fr_l.append(fr)
    #print(fr_l)
fn(w,fr_l)