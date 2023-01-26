
def fibonacci_top_down(n, memo=[0, 1]):
    if n <= len(memo):
        return memo[n - 1]
    memo.append(fibonacci_top_down(n - 1, memo) +
                fibonacci_top_down(n - 2, memo))
    return memo[n - 1]


def fibonacci_bottom_up(n):
    if n <= 2:
        return 1 if n == 2 else 0

    a, b = 0, 1
    while n > 2:
        a, b = b, a+b
        n = n - 1
    return b


def main():
    print(fibonacci_top_down(1), fibonacci_top_down(2), fibonacci_top_down(3),
          fibonacci_top_down(4), fibonacci_top_down(5), fibonacci_top_down(6),
          fibonacci_top_down(7), fibonacci_top_down(8), fibonacci_top_down(9))

    print(fibonacci_bottom_up(1), fibonacci_bottom_up(2),
          fibonacci_bottom_up(3), fibonacci_bottom_up(4),
          fibonacci_bottom_up(5), fibonacci_bottom_up(6),
          fibonacci_bottom_up(7), fibonacci_bottom_up(8),
          fibonacci_bottom_up(9))


if __name__ == '__main__':
    main()
