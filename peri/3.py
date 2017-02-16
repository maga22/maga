import math
a=int(input("Введите A:"))
b=int(input("Введите B:"))
c=int(input("Введите C:"))
D=((b**2)-(4*(a*c)))
if D<0:
    print("Нет корней")
 
if D==0:
    x=((-b)/(2*a))
    print(x)

if D>0:
    x1=((-b)-(math.sqrt(D)))//(2*a)
    x2=((-b)+(math.sqrt(D)))//(2*a)
    print("x1:", x1)
    print("x2:", x2)

    
