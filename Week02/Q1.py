#Write a Python function called getFibonacciNumbers(n) that generates a list of all Fibonacci numbers less than or equal to n. Fibonacci numbers are defined as: 
# • F_0 = 0 
# • F_1 = 1 
# • F_n = F_{n-1} + F_{n-2} for n \geq 2

#For example:
#getFibonacciNumbers(10)
# Output: [0, 1, 1, 2, 3, 5, 8]

def getFibonacciNumbers(n):
    if n < 0:
        return []
    fib_nums = [0,1]
    while True:
        next_fib = fib_nums[-1] + fib_nums[-2]
        if next_fib > n:
            break
        fib_nums.append(next_fib)
    return fib_nums if n >= 1 else [0]
    
print(getFibonacciNumbers(10))