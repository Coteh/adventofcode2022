day11 = __import__("11")

def test_day11_parse_single_monkey():
    data = day11.process_input("11/sample_small")
    assert len(data) == 1
    monkey = data[0]
    assert isinstance(monkey, day11.Monkey)
    assert monkey.no == 2
    assert monkey.items == [79, 60, 97]
    assert isinstance(monkey.worry_op, day11.WorryOperation)
    assert monkey.worry_op.left == "old"
    assert monkey.worry_op.right == 4
    assert monkey.test_value == 13
    assert monkey.true_monkey == 1
    assert monkey.false_monkey == 3


def test_day11_parse_multiple_monkies():
    data = day11.process_input("11/sample")
    assert len(data) == 4
    i = 0
    for monkey in data:
        assert monkey.no == i
        i += 1


def test_day11_worry_operation_multiplication():
    worry_op = day11.WorryOperation(2, "*", 3)
    assert worry_op.evaluate(0) == 6


def test_day11_worry_operation_multiplication_very_large():
    LARGE_NUMBER = int(1e100) ** 5000
    worry_op = day11.WorryOperation(
        LARGE_NUMBER, "*", LARGE_NUMBER)
    assert worry_op.evaluate(0) == LARGE_NUMBER * LARGE_NUMBER


def test_day11_worry_operation_addition():
    worry_op = day11.WorryOperation(2, "+", 3)
    assert worry_op.evaluate(0) == 5


def test_day11_worry_operation_addition_very_large():
    LARGE_NUMBER = int(1e100) ** 5000
    worry_op = day11.WorryOperation(
        LARGE_NUMBER, "+", LARGE_NUMBER)
    assert worry_op.evaluate(0) == LARGE_NUMBER + LARGE_NUMBER


def test_day11_worry_operation_with_left_old():
    worry_op = day11.WorryOperation("old", "*", 3)
    assert worry_op.evaluate(9) == 27


def test_day11_worry_operation_with_right_old():
    worry_op = day11.WorryOperation(2, "*", "old")
    assert worry_op.evaluate(9) == 18


def test_day11_worry_operation_with_two_old():
    worry_op = day11.WorryOperation("old", "*", "old")
    assert worry_op.evaluate(9) == 81


def test_day11_monkey_test_true():
    monkey = day11.Monkey(
        1, [12, 23, 34], day11.WorryOperation("old", "*", 4), 3, 9, 12)
    assert monkey.test(6) == True


def test_day11_monkey_test_false():
    monkey = day11.Monkey(
        1, [12, 23, 34], day11.WorryOperation("old", "*", 4), 3, 9, 12)
    assert monkey.test(4) == False


def test_day11_monkey_throwing_one_round():
    monkies = day11.process_input("11/sample")
    assert len(monkies) == 4
    day11.process_monkey_throwing(monkies, 1)
    day11.print_round_stats(monkies, 1)
    assert len(monkies[0].items) == 4
    assert len(monkies[1].items) == 6
    assert len(monkies[2].items) == 0
    assert len(monkies[3].items) == 0
    assert monkies[0].items == [20, 23, 27, 26]
    assert monkies[1].items == [2080, 25, 167, 207, 401, 1046]
    assert monkies[2].items == []
    assert monkies[3].items == []
