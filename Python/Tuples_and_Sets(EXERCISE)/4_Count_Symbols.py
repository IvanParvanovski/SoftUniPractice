def solve(text):
    characters_dict = dict()
    for symbol in text:
        if symbol not in characters_dict:
            characters_dict[symbol] = 0
        characters_dict[symbol] += 1

    return characters_dict


[print(f"{key}: {value} time/s") for key, value in sorted(solve(input()).items())]
