'''
Name : Subashree
Setno: 3
Question_no:8
Description:list of alphabets is sorted or not
'''


def is_abecedarian(x1):
  x=sorted(x1)
  print(x)
  if (x1==x):
    print("true")
  else:
    print("false")
x=raw_input("enter list:")
x1=list(x)
print(x1)
is_abecedarian(x1)