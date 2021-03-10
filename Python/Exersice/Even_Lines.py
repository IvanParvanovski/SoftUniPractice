def replace_symbols(line):
    line = line.replace('-', '@')
    line = line.replace(',', '@')
    line = line.replace('.', '@')
    line = line.replace('!', '@')
    line = line.replace('?', '@')
    text = line.split()
    return text[::-1]


def read_file(path):
    try:
        file = open(path, 'r')
        count = 0
        for line in file:
            if count % 2 == 0:
                print(' '.join(replace_symbols(line)))
            count += 1
        file.close()
    except FileNotFoundError:
        pass
    return


text_file_path = 'text.txt'
read_file(text_file_path)
