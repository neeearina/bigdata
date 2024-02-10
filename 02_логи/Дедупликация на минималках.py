headers = {
    "userid": "",
    "timestamp": "",
    "action": "",
    "value": "",
    "testids": ""
}
unique_logs: list[list] = []
mn = set()
with open("output.tsv", "w") as write_file:
    write_file.write("userid	timestamp	action	value	testids" + "\n")
    with open("log.dsv", "r") as read_file:
        for log_line in read_file.readlines():
            log_data = log_line.split()
            if len(log_data) == 4:
                del headers["testids"]
            for couple in log_data:
                k_v = couple.split("=")
                headers[k_v[0]] = k_v[1]
            st = "\t".join([v for v in headers.values()]) + "\n"
            if st not in mn:
                mn.add(st)
                write_file.write(st)
