#!/usr/bin/env python3

import json
import sys

# Read the JSON file line by line from stdin
for line in sys.stdin:
    try:
        if not line:
            continue
        line = line.strip().strip(',')
        # Convert the line (which is a string representing a JSON object) to a dictionary
        json_dict = json.loads(line)
        name = json_dict['name']
        runs = json_dict['runs']
        balls = json_dict['balls']
        local_strike_rate = (runs / balls) * 100
        print("%s\t%s" % (name, local_strike_rate))
    except Exception as e:
        sys.stderr.write("Error processing line: %s\n" % e)
