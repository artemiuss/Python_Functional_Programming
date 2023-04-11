from typing import Callable

from Essentials.TailFibonacci.tail_recursion import tail_call_optimized


def fibonacci_impl() -> Callable[[int], int]:
    @tail_call_optimized
    def fib_helper(depth: int, step: int, current: int, previous: int) -> int:
        if depth == step:
            return current
        else:
            return fib_helper(depth, step + 1, current + previous, current)

    def fib_fn(n: int) -> int:
        return n if n < 2 else fib_helper(n, 2, 1, 2)

    return fib_fn
