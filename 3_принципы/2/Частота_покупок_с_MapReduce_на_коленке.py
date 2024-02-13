from itertools import groupby
from dataclasses import dataclass


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
class UserData:
    userid: str
    frequency: int


def user_data_parser(line: str):
    row = line.strip().split("\t")

    if row[0] == "userid" or row[2] != "checkout":
        yield from ()
    else:
        yield UserData(userid=row[0], frequency=1)


def count_users_by_date(inp):
    count = 0
    userid = None
    for ud in inp:
        userid = ud.userid
        count += 1
    yield UserData(userid=userid, frequency=count)


def process(mrjob: SimpleMapReduce) -> SimpleMapReduce:
    return mrjob.map(user_data_parser) \
        .reduce(count_users_by_date, key=["userid"])


with open("log.tsv", "r") as input_stream:
    mrjob = process(SimpleMapReduce(input_stream))
    for item in mrjob.output():
        print(item.userid, item.frequency)
