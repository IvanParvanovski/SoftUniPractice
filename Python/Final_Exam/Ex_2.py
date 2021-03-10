import re
pattern_emoji = r"([:|*]{2})([A-Z][a-z]{2,})\1"
string = input()
result_emoji = re.findall(pattern_emoji, string)
result = re.findall(r"(\d)", string)

total = 1
for digit in result:
    total *= int(digit)

if result_emoji is not None:
    print(f"Cool threshold: {total}")
    print(f"{len(result_emoji)} emojis found in the text. The cool ones are:")

for emoji in result_emoji:
    emoji_total = 0
    for char in emoji[1]:
        emoji_total += ord(char)
    if emoji_total < total:
        result_emoji.remove(emoji)

if result_emoji is not None:
    for emoji in result_emoji:
        print(emoji[0] + emoji[1] + emoji[0])