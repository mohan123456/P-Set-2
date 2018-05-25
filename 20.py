m=list(input("char"))
b=[]
for i in m:
  if(i=='x'):
    b.append('a')
  elif(i=='y'):
    b.append('b')
  elif(i=='z'):
    b.append('c') 
  elif(i=='X'):
    b.append('A') 
  elif(i=='Y'):
    b.append('B') 
  elif(i=='Z'):
    b.append('C') 
  else:            
    c=(chr(ord(i)+3))
    b.append(c)
  
print("".join(b))  
