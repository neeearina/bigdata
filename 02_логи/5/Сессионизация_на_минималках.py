data: dict[str, set[set]] = {}  # userid: [{data}, {data}]
headers = ["userid", "timestamp", "action", "value", "testids", "sessionid"]
with open("output.tsv", "w") as write_file:
    write_file.write("\t".join(headers))
    with open("log.tsv", "r") as read_file:
        print()
        # for i in read_file.readlines()[1:]:
        #     for j in read_file.readlines():
        #         if i == j:
        #             existing_data = data.setdefault(i, set())
        #             existing_data.add({el for el in j.split()[1:]})

# надо перебирать файл двумя циклами - перебирать все строки связанные с одним юзером, ему расставлять значения
