def fizzbuzz(n):
    for i in range(1,n+1):
        if i % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizzbuzz(30)

##EXAMPLE WALKTHROUGH
"""
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
FizzBuzz
22
23
FizzBuzz
Buzz
26
FizzBuzz
28
29
FizzBuzz
"""