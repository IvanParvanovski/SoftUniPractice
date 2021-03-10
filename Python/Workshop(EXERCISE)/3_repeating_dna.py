def get_repeating_DNA(string):
    sequences = list()
    for index in range(len(string) - 10):
        sequence = string[index:index + 10]
        if sequence in string[index + 1:] and sequence not in sequences:
            sequences.append(sequence)
    return sequences

test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)

test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
result = get_repeating_DNA(test)
print(result)

test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)
