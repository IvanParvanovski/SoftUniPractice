import os


def create_dict_with_files(path):
    dict_to_create = {}
    for root, dirs, files in os.walk(path):
        if root.count(os.path.sep) - separator_count > 1:
            continue
        for file in files:
            extension = file.split('.')[-1]
            if extension not in dict_to_create:
                dict_to_create[extension] = []
            dict_to_create[extension].append(file)
    return dict_to_create


def create_string_to_write(dict_to_str):
    result = ''
    for key, value in sorted(dict_to_str.items()):
        result += f'.{key}\n'
        for file in sorted(value):
            result += f'- - - {file}\n'
    return result


def write_to_report(path, report):
    with open(path, 'w') as f:
        f.write(report)
    return


input_path = input()
separator_count = input_path.count(os.path.sep)
result_dictionary = create_dict_with_files(input_path)
result_string = create_string_to_write(result_dictionary)

# Desktop path for UNIX, macOS, Linux:

desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

# Desktop path for Windows:
# desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

report_path = desktop + os.path.sep + 'report.txt'

write_to_report(report_path, result_string)
