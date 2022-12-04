#!/usr/bin/env python

import sys

def process_input(file_name):
    with open(file_name) as f:
        data = f.read()
        sections_pairs = [data.split(",") for data in data.strip().split("\n")]
        parsed_section_pairs = []
        for sections_pair in sections_pairs:
            parsed_section_pair = []
            for sections in sections_pair:
                sections_parsed = [int(section) for section in sections.split("-")]
                parsed_section_pair.append(sections_parsed)
            parsed_section_pairs.append(parsed_section_pair)
        return parsed_section_pairs

def calculate_full_overlaps(sections_pairs):
    full_overlaps = 0
    for sections_pair in sections_pairs:
        section1 = sections_pair[0]
        section2 = sections_pair[1]
        if (section2[0] <= section1[0] and section2[1] >= section1[1]) or (section2[0] >= section1[0] and section2[1] <= section1[1]):
            full_overlaps += 1
    return full_overlaps

def calculate_overlaps(sections_pairs):
    overlaps = 0
    for sections_pair in sections_pairs:
        section1 = sections_pair[0]
        section2 = sections_pair[1]
        if (section2[0] >= section1[0] and section2[0] <= section1[1]) or (section1[1] >= section2[0] and section1[1] <= section2[1]) or (section1[0] >= section2[0] and section1[0] <= section2[1]) or (section2[1] >= section1[0] and section2[1] <= section1[1]):
            overlaps += 1
    return overlaps

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.stderr.write("Please provide input filename")
        sys.exit(1)
    data = process_input(sys.argv[1])
    # print(data)
    result = calculate_full_overlaps(data)
    print(result)
    result2 = calculate_overlaps(data)
    print(result2)
