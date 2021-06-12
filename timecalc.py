#!/usr/bin/env python3

from datetime import datetime, timedelta
import re

time_pattern = re.compile("^(# [\w\-]+:)(?:\s+__-?\d{1,2}:\d\d__)?\s+(\(([\d\s:\-,]+)\))")
output = []

with open("diary.md") as diary_file:
    line_n = 0
    for line in diary_file:
        line_n += 1
        match = time_pattern.match(line)
        if match:
            time_str = match.group(3)
            interval_strs = time_str.split(",")
            total_diff = timedelta(0)
            for interval_str in interval_strs:
                times = [datetime.strptime(t.strip(), "%H:%M") for t in interval_str.split("-")]
                if len(times) == 1:
                    now = datetime.now()
                    times.append(datetime(1900, 1, 1, now.hour, now.minute))
                elif len(times) != 2:
                    print("Warning, bad interval in line ", line_n, ": ", interval_str)
                    continue
                diff = times[1] - times[0]
                total_diff += diff
            hours, remainder = divmod(total_diff.total_seconds(), 3600)
            minutes, seconds = divmod(remainder, 60)
            output.append('{} __{}:{:02}__ {}\n'.format(match.group(1), int(hours), int(minutes), match.group(2)))
        else:
            output.append(line)

# print("".join(output))

with open("diary.md", "w") as diary_file:
    diary_file.write("".join(output))
