##scratch to practice dtnamic programming

import time

def fib_r(n):
    # take an int and returns the fib
    #
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fib_r(n-1) + fib_r(n-2)
    return result

def fib_dp(n, memo = {}):
    # take an int and returns the fib
    #
    # base case
    try:
        return memo[n]
    except KeyError:
        if n == 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = fib_dp(n-1, memo) + fib_dp(n-2, memo)
            memo[n] = result
        return result





if __name__ == '__main__':
    n = 10
    start = time.time()
    print("Actual Dynamic programming output:", fib_dp(n))
    end = time.time()
    print("it took: ", end - start)
    start = time.time()
    print("Actual recursive output:", fib_r(n))
    end = time.time()
    print("it took: ", end - start)

