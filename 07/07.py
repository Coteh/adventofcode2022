#!/usr/bin/env python

import sys
from enum import Enum

class FileType(Enum):
    DIR = 0
    FILE = 1

class FileNode(object):
    def __init__(self, file_type, file_name, file_size=0):
        self.name = file_name
        self.files = []
        self.type = file_type
        self.size = file_size
    def add_file(self, file):
        self.files.append(file)

def process_input(file_name):
    with open(file_name) as f:
        data = f.read()
        return [line.split(" ") for line in data.rstrip().split("\n")]

def get_resolved_node_name(dir_stack, node_name=""):
    if len(dir_stack) == 1:
        return "/" + node_name
    return "/" + "/".join(dir_stack[1:]) + ("/" + node_name if node_name != "" else "")

def process_terminal_lines(lines):
    file_tree = FileNode(FileType.DIR, "/")
    dir_dict = {
        "/": file_tree
    }

    last_command = ""
    dir_stack = []
    
    for line in lines:
        if line[0] == "$":
            # it is a command
            if line[1] == "cd":
                # print(dir_dict)
                cd_dir = line[2]
                if cd_dir == "..":
                    dir_stack.pop()
                else:
                    dir_stack.append(line[2])
                # print("Now in " + get_resolved_node_name(dir_stack))
            last_command = line[1]
        else:
            # it is an output
            if last_command == "ls":
                curr_dir = dir_dict[get_resolved_node_name(dir_stack)]
                if line[0] == "dir":
                    # it is a dir
                    new_dir = FileNode(FileType.DIR, line[1])
                    dir_dict[get_resolved_node_name(
                        dir_stack, line[1])] = new_dir
                    curr_dir.add_file(new_dir)
                else:
                    curr_dir.add_file(FileNode(FileType.FILE, line[1], int(line[0])))

    return file_tree, dir_dict

def calculate_directory_size(file_tree: FileNode):
    if file_tree is None:
        return 0
    total_size = 0
    for node in file_tree.files:
        if node.type == FileType.DIR:
            total_size += calculate_directory_size(node)
        else:
            total_size += node.size
    file_tree.size = total_size
    return total_size

def print_file_tree(file_tree: FileNode, tab_level=0):
    if file_tree is None:
        return
    print("".join([" "] * tab_level) + "- " + file_tree.name +
          " (dir, size= " + str(file_tree.size) + ")")
    for node in file_tree.files:
        if node.type == FileType.DIR:
            print_file_tree(node, tab_level + 1)
        else:
            print("".join([" "] * (tab_level + 1)) + "- " + node.name + " (file, size= " + str(node.size) + ")")


def calculate_candidate_directories(dir_dict):
    total_size = 0
    for resolved_path in dir_dict:
        if resolved_path == "/":
            continue
        dir = dir_dict[resolved_path]
        # print(dir)
        if dir.size <= 100000:
            total_size += dir.size
    return total_size

def calculate_smallest_dir_to_delete(dir_dict, total_size, required_free):
    total_free = total_size - dir_dict["/"].size

    candidates_for_deletion = []

    for resolved_path in dir_dict:
        dir = dir_dict[resolved_path]
        if dir.size + total_free >= required_free:
            candidates_for_deletion.append(dir.size)

    candidates_for_deletion.sort()
    # print(candidates_for_deletion)

    return candidates_for_deletion[0]

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.stderr.write("Please provide input filename")
        sys.exit(1)
    data = process_input(sys.argv[1])
    # print(data)
    file_tree, dir_dict = process_terminal_lines(data)
    calculate_directory_size(file_tree)
    # print_file_tree(file_tree)
    result = calculate_candidate_directories(dir_dict)
    print(result)
    result2 = calculate_smallest_dir_to_delete(dir_dict, 70000000, 30000000)
    print(result2)

