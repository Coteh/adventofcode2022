#!/usr/bin/env python

import sys, functools

def process_input(file_name):
    with open(file_name) as f:
        data = f.read()
        return [int(x) if x != "" else x for x in data.split("\n")]

def calculate_most_calories(calorie_input):
    most_calories = 0
    curr_calorie_count = 0
    for val in calorie_input:
        if val == "":
            if curr_calorie_count > most_calories:
                most_calories = curr_calorie_count
            curr_calorie_count = 0
            continue
        curr_calorie_count += val
    return most_calories

def calculate_top_3_calories(calorie_input):
    calorie_counts = []
    curr_calorie_count = 0
    for val in calorie_input:
        if val == "":
            calorie_counts.append(curr_calorie_count)
            curr_calorie_count = 0
            continue
        curr_calorie_count += val
    calorie_counts.sort(reverse=True)
    return functools.reduce(lambda x, y: x+y, calorie_counts[:3])

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.stderr.write("Please provide input filename")
        sys.exit(1)
    data = process_input(sys.argv[1])
    # print(data)
    answer = calculate_most_calories(data)
    print(answer)
    answer2 = calculate_top_3_calories(data)
    print(answer2)
