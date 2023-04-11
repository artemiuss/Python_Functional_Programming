from typing import Callable


def factorial_impl() -> Callable[[int], int]:
    def fact(n: int) -> int:
        if n == 0:
            return 1
        elif n < 3:
            return n
        else:
            return n * fact(n-1)
    return fact
