a=int(input("size"))
b=[]
for i in range(0,a):
  c=int(input("number"))
  b.append(c)
d=[]  
for i in b:
  if(b.count(i)!=1):
    continue
  else:
    d.append(i)
print("".join(str(x) for x in d))    
