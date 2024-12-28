#!/usr/bin/env python

import sys, copy, functools

# NOTE: I read from the subreddit that for part 2, I needed to use modular arithemtic.
# I was still struggling with the solution, then read that I needed to take the least common denominator
# of all the monkey test values then take the result of the worry operation and modulus it by that number.

class WorryOperation(object):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    def evaluate(self, item_value):
        self.left_value = item_value if self.left == "old" else self.left
        self.right_value = item_value if self.right == "old" else self.right
        if self.op == "*":
            return self.left_value * self.right_value
        else: # +
            return self.left_value + self.right_value

class Monkey(object):
    def __init__(self, no, starting_items, worry_op, test_value, true_monkey, false_monkey):
        self.no = no
        self.items = starting_items
        self.worry_op = worry_op
        self.test_value = test_value
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspect_count = 0
    def test(self, item):
        return item % self.test_value == 0

def process_input(file_name):
    with open(file_name) as f:
        data = f.read()
        monkey_strings = data.rstrip().split("\n\n")
        monkies = []

        for monkey_string in monkey_strings:
            monkey_string_parts = monkey_string.split("\n")

            monkey_no = int(monkey_string_parts[0].split(" ")[1].split(":")[0])

            starting_items = [int(item.strip()) for item in monkey_string_parts[1].split(":")[1].split(",")]

            operation_tokens = monkey_string_parts[2].split(":")[1].lstrip().split(" ")

            worry_op_left = int(
                operation_tokens[2]) if operation_tokens[2] != "old" else operation_tokens[2]
            worry_op_right = int(
                operation_tokens[4]) if operation_tokens[4] != "old" else operation_tokens[4]
            worry_op_operator = operation_tokens[3]
            worry_op = WorryOperation(worry_op_left, worry_op_operator, worry_op_right)
            
            test_value = int(
                monkey_string_parts[3].split("divisible by")[1].lstrip())
            true_monkey = int(monkey_string_parts[4].split(
                "throw to monkey")[1].lstrip())
            false_monkey = int(monkey_string_parts[5].split(
                "throw to monkey")[1].lstrip())

            monkey = Monkey(monkey_no, starting_items, worry_op, test_value, true_monkey, false_monkey)
            monkies.append(monkey)

        return monkies

def print_round_stats(monkies, round_num):
    print("Round " + str(round_num) + " Stats")
    for monkey in monkies:
        print("Monkey " + str(monkey.no) + ": " + ", ".join([str(item) for item in monkey.items]))
    for monkey in monkies:
        print("Monkey " + str(monkey.no) + " inspected items " + str(monkey.inspect_count) + " times.")


def process_monkey_throwing(monkies, num_rounds, very_worried=False, lcd=None):
    for i in range(0, num_rounds):
        for monkey in monkies:
            for item in monkey.items:
                if very_worried:
                    new_worry_level = monkey.worry_op.evaluate(item) % lcd
                else:
                    new_worry_level = monkey.worry_op.evaluate(
                        item) // 3
                monkey.inspect_count += 1
                if monkey.test(new_worry_level):
                    monkies[monkey.true_monkey].items.append(new_worry_level)
                else:
                    monkies[monkey.false_monkey].items.append(new_worry_level)
            monkey.items = []

def multiply_highest_inspect_counts(monkies):
    inspect_counts = sorted([monkey.inspect_count for monkey in monkies], reverse=True)

    return inspect_counts[0] * inspect_counts[1]

def lcd_nums(nums):
    return functools.reduce(lambda x, y: x * y, nums)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.stderr.write("Please provide input filename")
        sys.exit(1)
    monkies = process_input(sys.argv[1])
    monkies2 = copy.deepcopy(monkies)
    PART_1_ROUNDS = 20
    PART_2_ROUNDS = 10000
    lcd = lcd_nums([monkey.test_value for monkey in monkies])

    process_monkey_throwing(monkies, PART_1_ROUNDS)
    # print_round_stats(monkies, PART_1_ROUNDS)
    print(multiply_highest_inspect_counts(monkies))

    process_monkey_throwing(monkies2, PART_2_ROUNDS, True, lcd)
    # print_round_stats(monkies2, PART_2_ROUNDS)
    print(multiply_highest_inspect_counts(monkies2))
