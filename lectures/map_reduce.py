from dataclasses import dataclass
from typing import Iterable, Callable


@dataclass
class Number:
    value: int


input_stream = [
    Number(9), Number(34),
    Number(90), Number(46),
    Number(120), Number(11),
]


def digit_mapper(num: Number) -> Iterable[Number]:
    if 10 <= num.value <= 99:
        yield Number(num.value % 10),
        yield Number(num.value // 10 % 10)


def flatten(stream: Iterable[Iterable]) -> Iterable:
    for it in stream:
        for element in it:
            yield element


def run_map(mapper: Callable, input_stream: Iterable) -> Iterable:
    return flatten(map(mapper, input_stream))


print(list(run_map(digit_mapper, input_stream)))
