#!/usr/bin/env python

import sys

def process_input(file_name):
    with open(file_name) as f:
        data = f.read()
        return [[int(tree) for tree in line] for line in data.rstrip().split("\n")]

def calculate_number_of_visible_trees(tree_grid):
    total_count = (len(tree_grid) * 2) + ((len(tree_grid[0]) - 2) * 2)

    for i in range(1, len(tree_grid) - 1):
        for j in range(1, len(tree_grid[i]) - 1):
            curr_tree = tree_grid[i][j]
            # print(curr_tree)
            sides_visible = 4
            for k in range(j + 1, len(tree_grid[0])):
                # print("->" + str(tree_grid[i][k]))
                if tree_grid[i][k] >= curr_tree:
                    sides_visible -= 1
                    break
            for k in range(i + 1, len(tree_grid)):
                # print("v" + str(tree_grid[k][j]))
                if tree_grid[k][j] >= curr_tree:
                    sides_visible -= 1
                    break
            for k in range(j - 1, -1, -1):
                # print("<-" + str(tree_grid[i][k]))
                if tree_grid[i][k] >= curr_tree:
                    sides_visible -= 1
                    break
            for k in range(i - 1, -1, -1):
                # print("^" + str(tree_grid[k][j]))
                if tree_grid[k][j] >= curr_tree:
                    sides_visible -= 1
                    break
            if sides_visible > 0:
                # print("This tree is visible")
                total_count += 1

    return total_count

def calculate_scenic_score(tree_grid):
    # going to skip trees on the edges as at least one of their directions
    # provides 0 viewable trees, for a total score of 0

    highest_score = 0

    for i in range(1, len(tree_grid) - 1):
        for j in range(1, len(tree_grid[i]) - 1):
            curr_tree = tree_grid[i][j]
            # print(curr_tree)
            ls, rs, ds, us = 0, 0, 0, 0
            for k in range(j + 1, len(tree_grid[0])):
                # print("->" + str(tree_grid[i][k]))
                rs += 1
                if tree_grid[i][k] >= curr_tree:
                    break
            for k in range(i + 1, len(tree_grid)):
                # print("v" + str(tree_grid[k][j]))
                ds += 1
                if tree_grid[k][j] >= curr_tree:
                    break
            for k in range(j - 1, -1, -1):
                # print("<-" + str(tree_grid[i][k]))
                ls += 1
                if tree_grid[i][k] >= curr_tree:
                    break
            for k in range(i - 1, -1, -1):
                # print("^" + str(tree_grid[k][j]))
                us += 1
                if tree_grid[k][j] >= curr_tree:
                    break
            score = ls * rs * ds * us
            if score > highest_score:
                highest_score = score
    
    return highest_score

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.stderr.write("Please provide input filename")
        sys.exit(1)
    data = process_input(sys.argv[1])
    # print(data)
    result = calculate_number_of_visible_trees(data)
    print(result)
    result2 = calculate_scenic_score(data)
    print(result2)
