a=input("num")
b=[]
c=('a', 'e', 'i' ,'o' , 'u' )
for i in a:
 if i in c:
   continue
 else:  
   b.append(i)
x=("".join(b))   
print(x[::-1])

