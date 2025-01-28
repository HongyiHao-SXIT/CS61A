def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    num = n
    while k!=0:
        num = num * n
        n = n-1
        k = k - 1
    return n

print(falling(6, 3))  # 输出应为 120
print(falling(4, 3))  # 输出应为 24
print(falling(4, 1))  # 输出应为 4
print(falling(4, 0))  # 输出应为 1