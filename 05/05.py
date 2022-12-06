#!/usr/bin/env python

import sys, copy

def process_input(file_name):
    with open(file_name) as f:
        data = f.read()
        parts = data.rstrip().split("\n\n")
        instructions = [line.split(" ") for line in parts[1].split("\n")]
        instructions_parsed = []
        for line in instructions:
            parsed_line = {
                'move': int(line[1]),
                'from': int(line[3]),
                'to': int(line[5]),
            }
            instructions_parsed.append(parsed_line)
        split_stack_str = parts[0].split("\n")
        num_stacks = int(split_stack_str[-1].strip().split(" ")[-1])
        # print(num_stacks)
        stacks = []
        for i in range(0,num_stacks):
            stack = []
            stacks.append(stack)
            for line in split_stack_str[:-1]:
                item = line[i * 3 + (i + 1)]
                if item != " ":
                    stack.append(item)
        return stacks, instructions_parsed

def process_instructions_9000(stacks, instructions):
    for instruction in instructions:
        from_index = instruction['from'] - 1
        to_index = instruction['to'] - 1
        move_amount = instruction['move']
        # print("from_index", from_index)
        # print("to_index", to_index)
        # print("move_amount", move_amount)
        for _ in range(0,move_amount):
            to_stack = [stacks[from_index][0]]
            to_stack.extend(stacks[to_index])
            stacks[to_index] = to_stack
            stacks[from_index] = stacks[from_index][1:]
        # print(stacks)
    return ''.join([stack[0] for stack in stacks])

def process_instructions_9001(stacks, instructions):
    for instruction in instructions:
        from_index = instruction['from'] - 1
        to_index = instruction['to'] - 1
        move_amount = instruction['move']
        # print("from_index", from_index)
        # print("to_index", to_index)
        # print("move_amount", move_amount)
        to_stack = stacks[from_index][:move_amount]
        to_stack.extend(stacks[to_index])
        stacks[to_index] = to_stack
        stacks[from_index] = stacks[from_index][move_amount:]
        # print(stacks)
    return ''.join([stack[0] for stack in stacks])

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.stderr.write("Please provide input filename")
        sys.exit(1)
    stacks, instructions = process_input(sys.argv[1])
    stacks2 = copy.deepcopy(stacks)
    # print(stacks)
    # print(instructions)
    result = process_instructions_9000(stacks, instructions)
    # print(stacks)
    print(result)
    # print(stacks2)
    result2 = process_instructions_9001(stacks2, instructions)
    # print(stacks2)
    print(result2)
