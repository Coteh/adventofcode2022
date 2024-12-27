day10 = __import__("10")

def test_day10_parse():
    data = day10.process_input("10/sample_small")
    assert len(data) == 3
    assert data[0] == ["noop"]
    assert data[1] == ["addx", "3"]
    assert data[2] == ["addx", "-5"]


def test_day10_process_instructions():
    cpu = day10.CPU()
    instructions = [["noop"], ["addx", "3"], ["addx", "-5"]]
    day10.process_instructions(cpu, instructions)
    assert cpu.cycle == 6
    assert cpu.x == -1


def test_day10_1_sample():
    cpu = day10.CPU()
    instructions = day10.process_input("10/sample")
    day10.process_instructions(cpu, instructions)
    assert cpu.signal_strength_sum == 13140


def test_day10_1_input():
    cpu = day10.CPU()
    instructions = day10.process_input("10/input")
    day10.process_instructions(cpu, instructions)
    assert cpu.signal_strength_sum == 12460


def test_day10_2_sample():
    cpu = day10.CPU()
    instructions = day10.process_input("10/sample")
    day10.process_instructions(cpu, instructions)
    expected_lines = [
        "##..##..##..##..##..##..##..##..##..##..",
        "###...###...###...###...###...###...###.",
        "####....####....####....####....####....",
        "#####.....#####.....#####.....#####.....",
        "######......######......######......####",
        "#######.......#######.......#######....."
    ]
    for i in range(0, len(expected_lines)):
        assert cpu.draw_buffer[i] == expected_lines[i]
