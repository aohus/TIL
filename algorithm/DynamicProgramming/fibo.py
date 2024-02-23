def fibo_basic(n):
    if n < 3:
        return 1
    return fibo(n - 1) + fibo(n - 2)


memo = {1: 1, 2: 1}


def fibo_memo(n):
    if n in memo:
        return memo[n]
    memo[n] = fibo_memo(n - 2) + fibo_memo(n - 1)
    return memo[n]


def fibo_deco(func):
    memo = {1: 1, 2: 1}

    def inner(n):
        if n in memo:
            return memo[n]
        memo[n] = func(n)
        return memo[n]

    return inner


@fibo_deco
def fibo(n):
    if n < 3:
        return 1
    return fibo(n - 1) + fibo(n - 2)


print(fibo(10))
