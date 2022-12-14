#!/usr/bin/env python

import sys, json, functools

def process_input(file_name):
    with open(file_name) as f:
        data = f.read()
        return [[json.loads(item) for item in line.split("\n")] for line in data.rstrip().split("\n\n")]

# 1 -> right order
# -1 -> wrong order
# 0 -> array lengths are the same and no comparison made a decision
def compair(pair, level=0):
    left_list = pair[0]
    right_list = pair[1]
    # print("".join([" "] * level) + "- Compare " + str(left_list) + " vs " + str(right_list))
    for i in range(min(len(left_list), len(right_list))):
        left_value = left_list[i]
        right_value = right_list[i]
        # If left value is a list then recursively compare
        if isinstance(left_value, list):
            # If right value is not a list but left list is, then convert right value to a list element before comparing recursively
            if not isinstance(right_value, list):
                right_value = [right_value]
            nested_result = compair([left_value, right_value], level + 1)
            if nested_result != 0:
                return nested_result
        else:
            # Check if right value is a list instead, if so then convert left value to a list then recursively compare
            if isinstance(right_value, list):
                left_value = [left_value]
                nested_result = compair([left_value, right_value], level + 1)
                if nested_result != 0:
                    return nested_result
            else:
                # Otherwise they're both ints, compare them directly
                # print("".join([" "] * (level + 1)) + "-> Compare " + str(left_value) + " vs " + str(right_value))
                if left_value < right_value:
                    return 1
                elif left_value > right_value:
                    return -1
    # print("".join([" "] * (level + 1)) + "- Final check: " +
    #       str(len(left_list)) + ", " + str(len(right_list)))
    if len(left_list) < len(right_list):
        return 1
    elif len(left_list) > len(right_list):
        return -1
    else:
        return 0

def compair_items(item1, item2):
    return compair([item1, item2])

def get_summed_correct_pair_orderings(pairs):
    indices = []

    for i in range(len(pairs)):
        # print("== Pair " + str(i + 1) + " ==")
        if compair(pairs[i]) >= 0:
            indices.append(i + 1)
        #     print("Right order")
        # else:
        #     print("Wrong order")

    return functools.reduce(lambda x,y: x + y, indices)

def find_decoder_key(all_pairs):
    all_pairs.sort(key=functools.cmp_to_key(compair_items), reverse=True)

    result = 0

    for i in range(len(all_pairs)):
        pair = all_pairs[i]
        if len(pair) == 1 and (pair[0] == [2] or pair[0] == [6]):
            if result > 0:
                return result * (i + 1)
            else:
                result = i + 1

    return -1

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.stderr.write("Please provide input filename")
        sys.exit(1)
    pairs = process_input(sys.argv[1])
    # print(pairs)
    result = get_summed_correct_pair_orderings(pairs)
    print(result)
    all_pairs = [packets for pair in pairs for packets in pair]
    all_pairs.append([[2]])
    all_pairs.append([[6]])
    # print(all_pairs)
    result2 = find_decoder_key(all_pairs)
    print(result2)
