b = int(input("upper range : "))
z=[]
for num in range(2,b + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           if(b%num==0):
             z.append(num)
             print(num)
           else:
             continue
