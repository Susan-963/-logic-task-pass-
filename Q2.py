a = int(input("Please, Enter the Lowest Range Value: "))
b = int(input("Please, Enter the Upper Range Value: "))
for n in range(a,b + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)