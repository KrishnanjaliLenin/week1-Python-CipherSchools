a=True
if a==True:
  print("The value is true")
print("end")

a=False
if a==False:
  print("The value is true")
else:
  print("This value is false")

a=5
if a==3:
  print("The value is 3")
elif a==5:
  print("The value is 5")
else:
  print("This value is not 3 nor 5")

'''cx: int(inf,-inf)
G->x

a=x<0
b=x==0
c=x>0
a int b = b int c = a int c= phi
conditions are mutually exclusive'''



#if the above condition is true input 1 
#if the above condition is false input 0
a=int(input())
b=int(input())
c=int(input())

if a==0 and b==0 and c==0:
    print("Profile cannot be acessed")
elif a==0 and b==0 and c==1:
    print("Profile can be acessed")
elif a==0 and b==1 and c==1:
    print("Profile can be acessed")
elif a==0 and b==1 and c==0:
    print("Profile cannot be acessed")
elif a==1 and b==0 and c==1:
    print("Profile can be acessed")
elif a==1 and b==0 and c==0:
    print("Profile can be acessed")
elif a==1 and b==1 and c==0:
    print("Profile cannot be acessed")
elif a==1 and b==1 and c==1:
    print("Profile can be acessed")


