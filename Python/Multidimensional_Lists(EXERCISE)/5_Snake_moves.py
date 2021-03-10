from collections import deque


def solve(rows, columns, word):
    word_que = deque(word)

    for row in range(rows):
        new_word = deque()
        for col in range(columns):
            if row % 2 == 0:
                element = word_que.popleft()
                new_word.append(element)
                word_que.append(element)
            else:
                element = word_que.popleft()
                new_word.appendleft(element)
                word_que.append(element)
        print(''.join(new_word))


(user_rows, user_columns) = input().split()
string = input()

solve(int(user_rows), int(user_columns), string)
