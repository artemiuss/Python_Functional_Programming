from typing import Callable


def fibonacci_impl() -> Callable[[int], int]:
    def fib(n: int) -> int:
        return n if n < 2 else (fib(n-1) + fib(n-2))
    return fib
