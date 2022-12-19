
def fibonacci(n, memo=[0, 1]):
    if n <= len(memo):
        return memo[n - 1]
    memo.append(fibonacci(n - 1, memo) + fibonacci(n - 2, memo))
    return memo[n - 1]


def main():
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(4))
    print(fibonacci(5))
    print(fibonacci(6))
    print(fibonacci(7))


if __name__ == '__main__':
    main()
