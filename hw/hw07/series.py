
def fibonacci(n):
    '''
    Returns the nth number from the Fibonacci formula
    example: fibonacci(0) == 0
             fibonacci(1) == 1
             fibonacci(2) == 1
    '''
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    '''
    Returns the nth number from the Lucas formula
    example: Lucas(0) == 2
             Lucas(1) == 1
             lucas(2) == 3
    '''
    if (n == 0):
        return 2
    elif (n == 1):
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, seq1=0, seq2=1):
    '''
    Returns the the sum of the two series together and compares the two.
    Calling the function with no secondary parameters will default it to
    Fibonacci
    example:  sum_series(0, 10, 20) == 10)
              sum_series(1, 10, 20) == 20)
              sum_series(2, 10, 20) == 30)
    '''
    if (n == 0):
        return seq1
    elif (n == 1):
        return seq2
    else:
        return sum_series(n - 1, seq1, seq2) +  \
            sum_series(n - 2, seq1, seq2)
