def print_boss_and_title():
    checked_boss = result.group('boss')
    checked_title = result.group('title')
    print(f"{checked_boss}, The {checked_title}")
    print(f">> Strength: {len(checked_boss)}")
    print(f">> Armour: {len(checked_title)}")

import re
boss_pattern = r"\|(?P<boss>[A-Z]{4,})\|"
separator = r":"
title_pattern = r"\#(?P<title>[a-zA-Z]+[ ][a-zA-Z]+)\#"
pattern = boss_pattern + separator + title_pattern

bosses_count = int(input())

for _ in range(bosses_count):
    boss = input()
    result = re.search(pattern, boss)
    if result is not None:
        print_boss_and_title()
    else:
        print("Access denied!")
