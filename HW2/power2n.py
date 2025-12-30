# 方法 1
def power2n(n):
    return 2**n

# 方法 2a：用遞迴
def power2n(n):
    if n == 0:
        return 1
    return power2n(n-1) + power2n(n-1)

# 方法2b：用遞迴
def power2n(n):
    if n == 0:
        return 1
    return 2 * power2n(n-1)

# 方法 3：用遞迴+查表
memo = {}

def power2n(n):
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = power2n(n-1) + power2n(n-1)
    return memo[n]
