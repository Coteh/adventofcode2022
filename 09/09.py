#!/usr/bin/env python

import sys, math

def process_input(file_name):
    with open(file_name) as f:
        data = f.read()
        result = [line.split(" ") for line in data.rstrip().split("\n")]
        for line in result:
            line[1] = int(line[1])
        return result

def process_rope_bridge(rope_bridge, num_bodies=1):
    h_pos = [0, 0]
    b_pos_arr = [[0, 0].copy() for _ in range(0, num_bodies)]

    t_pos_dic = {}
    t_pos_dic[str(b_pos_arr[-1])] = 1

    for motion in rope_bridge:
        direction = motion[0]
        steps = motion[1]
        projected_h_pos = h_pos.copy()
        h_mov = [0, 0]
        if direction == "R":
            projected_h_pos[0] += steps
            h_mov[0] = 1
        elif direction == "U":
            projected_h_pos[1] -= steps
            h_mov[1] = -1
        elif direction == "L":
            projected_h_pos[0] -= steps
            h_mov[0] = -1
        else:  # D
            projected_h_pos[1] += steps
            h_mov[1] = 1

        while h_pos[0] != projected_h_pos[0] or h_pos[1] != projected_h_pos[1]:

            h_pos[0] += h_mov[0]
            h_pos[1] += h_mov[1]

            i = 1
            for b_pos in b_pos_arr:
                prev_pos = h_pos if i == 1 else b_pos_arr[i - 2]
                dist_vec = [prev_pos[0] - b_pos[0], prev_pos[1] - b_pos[1]]
                dist = math.sqrt((dist_vec[0]) ** 2 + (dist_vec[1]) ** 2)

                if dist >= 2.0:
                    t_mov = [dist_vec[0] / dist, dist_vec[1] / dist]
                    if t_mov[0] > 0:
                        t_mov[0] = math.ceil(t_mov[0])
                    else:
                        t_mov[0] = math.floor(t_mov[0])
                    if t_mov[1] > 0:
                        t_mov[1] = math.ceil(t_mov[1])
                    else:
                        t_mov[1] = math.floor(t_mov[1])
                    b_pos[0] += t_mov[0]
                    b_pos[1] += t_mov[1]

                i += 1
            
            t_pos_dic[str(b_pos_arr[-1])] = 1

    return len(t_pos_dic)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.stderr.write("Please provide input filename")
        sys.exit(1)
    data = process_input(sys.argv[1])
    # print(data)
    result = process_rope_bridge(data, 1)
    print(result)
    result2 = process_rope_bridge(data, 9)
    print(result2)
