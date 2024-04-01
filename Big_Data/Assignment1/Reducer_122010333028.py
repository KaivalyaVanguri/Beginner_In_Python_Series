#!/usr/bin/env python3

import sys

current_name = None
total_strike_rate = 0
total_matches = 0

for line in sys.stdin:
    try:
        name, local_strike_rate = line.strip().split('\t')
        local_strike_rate = float(local_strike_rate)

        if current_name == name:
            total_strike_rate += local_strike_rate
            total_matches += 1
        else:
            if current_name:
                
                average_strike_rate = total_strike_rate / total_matches
                print('%s\t%.3f' % (current_name, average_strike_rate))
            
            current_name = name
            total_strike_rate = local_strike_rate
            total_matches = 1
    except Exception as e:
        
        sys.stderr.write("Error processing line: {}\n".format(line.strip()))
        sys.stderr.write(str(e) + "\n")

# Do not forget the shebang line
if current_name:
    average_strike_rate = total_strike_rate / total_matches
    print('%s\t%.3f' % (current_name, average_strike_rate))
