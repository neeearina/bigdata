import csv
import typing


class UniqueUsers:
    """Класс для определения самого популярного спектакля"""

    def __init__(self):
        self.__dictionary: dict[str, set] = {}

    @staticmethod
    def normalizer_phone_number(phone_number: str) -> typing.Union[str]:
        """Нормализует номер телефона"""
        digits = [char for char in phone_number if char.isdigit()]
        if len(digits) == 11 and digits[0] == "8":
            return "+7" + "".join(digits[1:])
        elif len(digits) == 10:
            return "+7" + "".join(digits)
        return ""

    def create_dictionary(self) -> None:
        """Создает словарь с уникальными телефонными номерами
        для каждого спектакля. Количество номеров телефонов -
        количество покупок билетов на спектакль"""
        with open("ticket_logs.csv", "r") as csv_file:
            csvreader = csv.reader(csv_file)
            for row in csvreader:
                normal_number = self.normalizer_phone_number(row[1])
                if normal_number:
                    self.__dictionary.setdefault(row[0], set()).add(normal_number)

    def print_result(self) -> None:
        """Функция подсчитывает самое большое количество
        покупок билетов на спектакль"""
        quantity = []
        for k, v in self.__dictionary.items():
            quantity.append(len(v))
        print(max(quantity))


unique = UniqueUsers()
unique.create_dictionary()
unique.print_result()
