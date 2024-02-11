import re

unique_logs: set = set()
count = 0


def add_unique_logs(user_id, time):
    global count
    log = (user_id, time)
    if log not in unique_logs:
        unique_logs.add(log)
        count += 1


def long_line(line):
    global count
    split_data = line.split()
    new_data = []
    for i in range(0, len(split_data) - 1):
        if i % 2 == 0 and i != 0 and i != len(split_data):
            match = re.match(r"([a-zA-Z]+)(\d+)", split_data[i])
            if match:
                action_part = match.group(1)
                id_part = match.group(2)
                new_data.append(action_part)
                new_data.append(id_part)
                continue
        new_data.append(split_data[i])
    for i in range(2, len(new_data), 3):
        if new_data[i] == "checkout" or new_data[i] == "checkᝃut":
            add_unique_logs(new_data[i - 2], new_data[i - 1])


with open("user_activity_bad_log.tsv", "r") as file:
    for line in file.readlines():
        if line.strip() != "":
            if len(line) > 50:
                long_line(line)
                continue
            log_data = line.split()
            if log_data[2] == "checkout" or log_data[2] == "checkᝃut":
                if not log_data[0].isdigit():
                    log_data[0] = log_data[0].split("=")[1]
                add_unique_logs(log_data[0], log_data[1])

unique_users = {v[0] for v in unique_logs}
print(round(count / len(unique_users), 5))
