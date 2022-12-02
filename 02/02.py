#!/usr/bin/env python

import sys

matchups = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}

shape_map = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

shape_points = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3,
}

part_2_end_map = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

part_2_winner_matchups = {
    "A": "B",
    "B": "C",
    "C": "A",
}

part_2_loser_matchups = {
    "A": "C",
    "B": "A",
    "C": "B",
}

def process_input(file_name):
    with open(file_name) as f:
        data = f.read()
        return [x.split(" ") for x in data.split("\n")][:-1]

def calculate_total_score(guide):
    total_score = 0
    for round in guide:
        round_score = 0
        # print("Round: " + str(round))
        if matchups[round[0]] == round[1]:
            round_score += 6
        elif shape_map[round[0]] == round[1]:
            round_score += 3
        round_score += shape_points[round[1]]
        # print("Round score: " + str(round_score))
        total_score += round_score
    return total_score

def calculate_total_score_2(guide):
    total_score = 0
    for round in guide:
        round_score = 0
        # print("Round: " + str(round))
        if round[1] == "X":
            round_score += shape_points[part_2_loser_matchups[round[0]]]
        elif round[1] == "Y":
            round_score += shape_points[round[0]]
        else:
            round_score += shape_points[part_2_winner_matchups[round[0]]]
        round_score += part_2_end_map[round[1]]
        # print("Round score: " + str(round_score))
        total_score += round_score
    return total_score

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.stderr.write("Please provide input filename")
        sys.exit(1)
    data = process_input(sys.argv[1])
    # print(data)
    result = calculate_total_score(data)
    print(result)
    result2 = calculate_total_score_2(data)
    print(result2)
