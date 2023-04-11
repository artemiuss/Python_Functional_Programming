from typing import Callable


class Integer:
    def __init__(self, value: int):
        self.value = value


def is_pure(increment_fn: Callable[[Integer], Integer]) -> bool:
    if increment_fn(Integer(1)).value != Integer(2).value:
        return False
    if increment_fn(Integer(2)).value != Integer(3).value:
        return False
    if increment_fn(increment_fn(Integer(1))).value != Integer(3).value:
        return False

    input_val = Integer(1)
    res1 = increment_fn(input_val).value
    res2 = increment_fn(input_val).value
    if res1 != res2:
        return False

    return True


