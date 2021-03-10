from collections import deque


def solve(parenthesis):
    que = deque()
    for char in parenthesis:
        que.append(char)

    if len(que) % 2 == 0:
        index = 0
        is_valid = True
        while index < len(que):
            element = que[index]

            if element == "}":
                second_element = que[index - 1]
                if second_element == "{":
                    que.remove(element)
                    que.remove(second_element)
                    index -= 2
                else:
                    is_valid = False
                    break

            elif element == "]":
                second_element = que[index - 1]
                if second_element == "[":
                    que.remove(element)
                    que.remove(second_element)
                    index -= 2
                else:
                    is_valid = False
                    break

            elif element == ")":
                second_element = que[index - 1]
                if second_element == "(":
                    que.remove(element)
                    que.remove(second_element)
                    index -= 2
                else:
                    is_valid = False
                    break
            index += 1

        if is_valid:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


print(solve(list(input())))