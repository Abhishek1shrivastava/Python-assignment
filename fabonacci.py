def fib(n):
    if n==0 or n==1:
        return n
    else:
        return(fib(n-2)+fib(n-1))
a = int(input("a nuber till fib series has to be calculated:"))
for i in range(a):
    print(fib(i))