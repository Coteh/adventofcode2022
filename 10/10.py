#!/usr/bin/env python

import sys, math

class CPU(object):
    def __init__(self):
        self.x = 1
        self.cycle = 0
        self.curr_instruction = None
        self.curr_instruction_started = 0
        self.signal_strength_sum = 0
        self.draw_buffer = []

def process_input(file_name):
    with open(file_name) as f:
        data = f.read()
        return [line.split(" ") for line in data.rstrip().split("\n")]


def process_instructions(cpu, instructions):
    i = 0
    j = 0
    while 1:
        cpu.cycle += 1
        # print("cpu cycle " + str(cpu.cycle))
        # print("cpu x " + str(cpu.x))
        if cpu.curr_instruction is not None:
            # print("handling instruction " + str(cpu.curr_instruction))
            if cpu.curr_instruction[0] == "addx":
                if cpu.cycle >= cpu.curr_instruction_started + 2:
                    cpu.x += int(cpu.curr_instruction[1])
                    # print("X is now " + str(cpu.x) + ", " + str(cpu.cycle))
                    cpu.curr_instruction = None
            else: # noop
                cpu.curr_instruction = None
        if cpu.curr_instruction is None:
            if i >= len(instructions):
                break
            # print("instruction " + str(i))
            cpu.curr_instruction = instructions[i]
            cpu.curr_instruction_started = cpu.cycle
            # print("Picking up instruction " + str(cpu.curr_instruction))
            i += 1
        
        if cpu.cycle % (20 + (j * 40)) == 0:
            cpu.signal_strength_sum += cpu.cycle * cpu.x
            # print("strength is now " + str(cpu.signal_strength_sum) + " " + str([cpu.cycle, cpu.x]))
            j += 1

        crt_draw = (cpu.cycle - 1) % 40
        if crt_draw == 0:
            cpu.draw_buffer.append("")
        if crt_draw >= cpu.x - 1 and crt_draw <= cpu.x + 1:
            cpu.draw_buffer[-1] += "#"
        else:
            cpu.draw_buffer[-1] += "."

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.stderr.write("Please provide input filename")
        sys.exit(1)
    data = process_input(sys.argv[1])
    # print(data)
    cpu = CPU()
    result = process_instructions(cpu, data)
    print(cpu.signal_strength_sum)
    for line in cpu.draw_buffer:
        print(line)

