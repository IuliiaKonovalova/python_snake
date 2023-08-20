def fizzBuzz(n):
    for i in range(1,n+1):
        print(("Fizz" * (i%3==0) + "Buzz" * (i%5==0)) or i)

fizzBuzz(15)