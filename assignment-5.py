def factorial(n):
    f=1;
    for i in range(1,n+1):
        f=f*i
    return f
a=int(input("Enter a number: "))
ans=factorial(a)
print('Factorial of',a,'is:',ans)
