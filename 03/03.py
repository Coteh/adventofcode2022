#!/usr/bin/env python

import sys, math, functools

def process_input(file_name):
    with open(file_name) as f:
        data = f.read()
        return data.split("\n")

def get_item_priority(item):
    return 27 + ord(item) - ord("A") if item >= "A" and item <= "Z" else 1 + ord(item) - ord("a")

def process_rucksack_compartments(compartments_list):
    found_duplicates = []
    for compartments_pair in compartments_list:
        found_dict = {}
        for item in compartments_pair[0]:
            found_dict[item] = 1
        for item in compartments_pair[1]:
            if item in found_dict:
                found_duplicates.append(item)
                break
    return functools.reduce(lambda x,y: x + get_item_priority(y), found_duplicates, 0)

def process_rucksack_groups(compartment_groups):
    found_group_badges = []
    for group in rucksack_groups:
        if len(group) < 3:
            continue
        found = {}
        i = 0
        for rucksack in group:
            for item in rucksack:
                if i == 0 or (item in found and found[item] == i - 1):
                    found[item] = i
            i += 1   
        # print(found)
        for key in found:
            if found[key] == 2:
                found_group_badges.append(key)
    return functools.reduce(lambda x,y: x + get_item_priority(y), found_group_badges, 0)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.stderr.write("Please provide input filename")
        sys.exit(1)
    rucksacks = process_input(sys.argv[1])
    # print(rucksacks)
    compartment_pairs = [[rucksack[0:math.floor(len(rucksack) / 2)], rucksack[math.floor(len(rucksack) / 2):]] for rucksack in rucksacks]
    # print(compartment_pairs)
    result = process_rucksack_compartments(compartment_pairs)
    print(result)
    rucksack_groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
    # print(rucksack_groups)
    result2 = process_rucksack_groups(rucksack_groups)
    print(result2)