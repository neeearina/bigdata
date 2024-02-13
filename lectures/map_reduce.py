from dataclasses import dataclass


@dataclass
class Number:
    value: int


def digit_mapper(num: Number):
    if 10 <= num.value <= 99:
        return (
            Number(num.value % 10),
            Number(num.value // 10 % 10)
        )
    else:
        return []


def flatten(stream):
    result = []
    for it in stream:
        for element in it:
            result.append(element)
    return result


input_stream = [
    Number(9), Number(34),
    Number(90), Number(46),
    Number(120), Number(11),
]
output_stream = flatten(map(digit_mapper, input_stream))
print(list(output_stream))
