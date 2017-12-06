'''
Name : Subashree
Setno: 3
Question_no:9 
'''

def is_sorted(x1):
  x=sorted(x1)
  print(x)
  if (x1==x):
    print("true")
  else:
    print("false")
x=raw_input("enter list:")
x1=list(x)
print(x1)
is_sorted(x1)