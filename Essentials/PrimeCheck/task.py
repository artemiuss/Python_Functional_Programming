def is_prime(n: int) -> bool:
    def check_prime(n: int, div: int) -> bool:
        if n < 2:
            return False
        if div * div > n:
            return True
        if n % div == 0:
            return False
        return check_prime(n, div + 1)

    return check_prime(n, 2)
