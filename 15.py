a=list(input("string"))
b=[] 
for i in a:
  if(a.count(i)!=1):
    b.append(i)
    
  else:
    continue
print(max(b))   
