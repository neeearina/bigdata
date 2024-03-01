"""Сколько уникальных пользователей посетило сайт в каждый из дней"""
import typing

data: dict[str, typing.Union[set, int]] = {}

with open("logs.tsv", "r") as file:
    """Создаем словарь с данными о логах"""
    for log in file.readlines()[1:]:
        data_log = log.split()
        data.setdefault(data_log[1][:10], set()).add(data_log[0])

for k in sorted(data):
    print(f"{k}: {len(data[k])}")
