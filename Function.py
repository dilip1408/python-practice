def fibo(n):
    a=0
    b=1
    for x in range (n):
        a=b
        b=a+b
        print(a,'\n')
    return a
num=int(input("enter the value of n:"))
print(fibo(num))
