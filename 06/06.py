#!/usr/bin/env python

import sys

def process_input(file_name):
    with open(file_name) as f:
        data = f.read()
        return [letter for letter in data.strip()]

def calculate_unique_marker_position(stream, marker_length):
    for i in range(len(stream)):
        if i >= marker_length - 1:
            match = False
            for j in range(i - (marker_length - 1), i):
                for k in range(j + 1, i + 1):
                    # print("Checking " + str(j) + " and " + str(k))
                    if stream[j] == stream[k]:
                        match = True
                        break
                if match:
                   break
            if not match:
                return i + 1
    return 0

def calculate_start_of_packet_position(stream):
    return calculate_unique_marker_position(stream, 4)

def calculate_start_of_message_position(stream):
    return calculate_unique_marker_position(stream, 14)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.stderr.write("Please provide input filename")
        sys.exit(1)
    data = process_input(sys.argv[1])
    # print(data)
    result = calculate_start_of_packet_position(data)
    print(result)
    result2 = calculate_start_of_message_position(data)
    print(result2)
