import csv
import json


class Incidents:
    def __init__(self):
        self.__headers = ["creature", "place", "danger", "date"]
        self.__result = []

    def create_result_file(self):
        self.__result_data()
        self.__write_to_csv()

    def __result_data(self):
        with open("cases.json", "r") as json_file:
            json_data = json.load(json_file)
        for d in json_data:
            self.__result.append(
                [d["creature"], d["place"], d["danger"], d["date"]]
            )
        self.__result.sort(key=lambda item: item[3], reverse=True)

    def __write_to_csv(self):
        with open("incidents.csv", "w") as csv_file:
            csvwriter = csv.writer(csv_file)
            csvwriter.writerow(self.__headers)
            for row in self.__result:
                csvwriter.writerow(row)


incident = Incidents()
incident.create_result_file()
