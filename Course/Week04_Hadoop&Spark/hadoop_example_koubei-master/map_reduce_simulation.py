import os
from read_inputs import read_inputs

def sorted_map_file(file_path, key=lambda x: x):
    wait_sorted = []
    with open(file_path, 'r') as file:
        wait_sorted.extend(list(read_inputs(file)))

    with open(file_path, 'w') as file:
        words_sorted = sorted(wait_sorted, key=key)
        for words in words_sorted:
            print(*words, file=file, sep='\t')


def test_map_reduce(file_path_list, mapper_py, reduce_py, mapper_result, reducer_result, \
                    key=lambda x: x[0], python_compile='python -c ', python_execute='python '):
    # print(os.getcwd())
    input_file_command = []
    if len(file_path_list) == 1:
        command = "\"print(open('" + file_path_list[0] + "').read())\""
        input_file_command.append(command)
    elif len(file_path_list) == 2:
        for i, path in enumerate(file_path_list):
            if i == 0:
                command = "\"print(open('" + path + "').read(), end='')\""
                # open(command, )
                input_file_command.append(command)
            else:
                command = "\"print(open('" + path + "').read())\""
                input_file_command.append(command)

    input_file_command = ";".join(input_file_command)

    os.system(python_compile + input_file_command + '|' + python_execute + mapper_py + '>' \
              + mapper_result)

    if reduce_py:
        sorted_map_file(mapper_result, key=key)
        read_mapfile = "\"print(open('" + mapper_result + "').read(), sep='\t')\""
        os.system(python_compile + read_mapfile + '|' + python_execute + reduce_py + '>' \
                  + reducer_result)

    print(file_path_list, ' process finished!')