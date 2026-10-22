import re
from pprint import pprint

logs = [
    "2026-09-24 10:15:32 INFO User 123 logged in",
    "2026-09-24 10:16:04 ERROR User 456 authentication failed",
    "2026-09-24 10:17:21 INFO User 123 opened page",
    "2026-09-24 10:18:45 WARNING User 789 too many requests",
    "2026-09-24 10:19:02 ERROR User 123 database connection failed",
]

def extract_logs(list):
    for i in range(len(list)):
        match = re.fullmatch(r'(?P<datetime>[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}) '
                          r'(?P<level>INFO|ERROR|WARNING) ' \
                          r'User (?P<user_id>\d+) ' \
                          r'(?P<message>.+)', list[i])
        if match:
            pprint(match.groupdict(), sort_dicts=False)

extract_logs(logs)