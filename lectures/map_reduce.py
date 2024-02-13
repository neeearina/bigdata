from dataclasses import dataclass


@dataclass
class Number:
    value: int


input_stream = [
    Number(9), Number(34),
    Number(90), Number(46),
    Number(120), Number(11),
]
output_stream = []
for item in input_stream:
    if 10 <= item.value <= 99:
        output_stream.append(Number(item.value % 10))
        output_stream.append(Number(item.value // 10 % 10))

print(output_stream)
