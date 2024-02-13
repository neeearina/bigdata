from itertools import groupby
from dataclasses import dataclass
from datetime import date


def flatten(inp):
    for it in inp:
        for item in it:
            yield item


def run_map(mapper, input_stream):
    return flatten(map(mapper, input_stream))


def run_reduce(reducer, input_stream, key: [str]):
    def key_func(item):
        return tuple(getattr(item, k) for k in key)

    sorted_stream = sorted(input_stream, key=key_func)
    grouped_stream = groupby(sorted_stream, key=key_func)
    return flatten(map(lambda x: reducer(x[1]), grouped_stream))


class SimpleMapReduce:
    def __init__(self, stream):
        self._stream = stream

    def map(self, mapper):
        self._stream = run_map(mapper, self._stream)
        return self

    def reduce(self, reducer, key):
        self._stream = run_reduce(reducer, self._stream, key)
        return self

    def output(self):
        return self._stream


@dataclass
class ValueByMonth:
    month: date
    value: float


def user_data_parser(line: str):
    row = line.strip().split("\t")

    if row[0] == "userid" or row[2] != "checkout":
        yield from ()
    else:
        split_date = row[1].split("-")
        year_month = "-".join([split_date[0], split_date[1]])
        yield ValueByMonth(month=year_month, value=float(row[3]))


def count_users_by_value(inp):
    count = 0
    date = None
    for d in inp:
        date = d.month
        count += d.value
    yield ValueByMonth(month=date, value=count)


def process(mrjob: SimpleMapReduce) -> SimpleMapReduce:
    return mrjob.map(user_data_parser) \
        .reduce(count_users_by_value, key=["month"])


with open("log.tsv", "r") as input_stream:
    mrjob = process(SimpleMapReduce(input_stream))
    for item in mrjob.output():
        print(item.month, item.value)
