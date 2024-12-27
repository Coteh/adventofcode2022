day13 = __import__("13")

def test_day13_parse():
    data = day13.process_input("13/sample")
    expected_data = [
        [
            [1,1,3,1,1],
            [1, 1, 5, 1, 1]
        ],
        [
            [[1],[2,3,4]],
            [[1],4],
        ],
        [
            [9],
            [[8, 7, 6]],
        ],
        [
            [[4, 4], 4, 4],
            [[4, 4], 4, 4, 4],
        ],
        [
            [7, 7, 7, 7],
            [7, 7, 7],
        ],
        [
            [],
            [3],
        ],
        [
            [[[]]],
            [[]],
        ],
        [
            [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
            [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
        ]
    ]
    assert len(data) == len(expected_data)
    for i in range(len(expected_data)):
        print(data[i])
        assert data[i] == expected_data[i]

def test_day13_pair_comparison_ints():
    pair = [
        [1, 1, 3, 1, 1],
        [1, 1, 5, 1, 1],
    ]
    assert day13.compair(pair) == 1
    pair = [
        [1, 1, 5, 1, 1],
        [1, 1, 3, 1, 1],
    ]
    assert day13.compair(pair) == -1


def test_day13_pair_comparison_unequal_elements():
    pair = [
        [1, 1, 1],
        [1, 1, 1, 1],
    ]
    assert day13.compair(pair) == 1
    pair = [
        [1, 1, 1, 1],
        [1, 1, 1],
    ]
    assert day13.compair(pair) == -1


def test_day13_pair_comparison_list_elements():
    pair = [
        [[1, 1, 3, 1, 1]],
        [[1, 1, 5, 1, 1]],
    ]
    assert day13.compair(pair) == 1
    pair = [
        [[1, 1, 5, 1, 1]],
        [[1, 1, 3, 1, 1]],
    ]
    assert day13.compair(pair) == -1


def test_day13_pair_comparison_list_elements_unequal_length():
    pair = [
        [[1, 1, 1, 1]],
        [[1, 1, 1, 1, 1]],
    ]
    assert day13.compair(pair) == 1
    pair = [
        [[1, 1, 1, 1, 1]],
        [[1, 1, 1, 1]],
    ]
    assert day13.compair(pair) == -1


def test_day13_pair_comparison_list_element_and_int_value():
    pair = [
        [1],
        [[2]],
    ]
    assert day13.compair(pair) == 1
    pair = [
        [[2]],
        [1],
    ]
    assert day13.compair(pair) == -1


def test_day13_pair_comparison_list_elements_iterates_all_elements():
    pair = [
        [[1], [2, 3, 4]],
        [[1], 1],
    ]
    assert day13.compair(pair) == -1
    pair = [
        [[1], 2],
        [[1], [1, 3, 4]],
    ]
    assert day13.compair(pair) == -1


def test_day13_pair_comparison_empty_lists():
    pair = [
        [[]],
        [[]],
    ]
    assert day13.compair(pair) == 0


def test_day13_pair_comparison_empty_list_and_other_with_values():
    pair = [
        [],
        [3],
    ]
    assert day13.compair(pair) == 1
    pair = [
        [],
        [[]],
    ]
    assert day13.compair(pair) == 1

    pair = [
        [3],
        [],
    ]
    assert day13.compair(pair) == -1
    pair = [
        [[]],
        [],
    ]
    assert day13.compair(pair) == -1


def test_day13_pair_comparison_empty():
    pair = [
        [],
        [],
    ]
    assert day13.compair(pair) == 0


def test_day13_inner_left_list_shorter_than_inner_right_list():
    pair = [
        [[1], [4]],
        [[1, 1], [3]]
    ]
    assert day13.compair(pair) == 1
