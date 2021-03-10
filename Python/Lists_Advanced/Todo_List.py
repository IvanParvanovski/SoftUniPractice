command = input()
todo_list = list()

while command != "End":
    command_list = command.split("-", maxsplit=1)
    importance = int(command_list[0])
    task = command_list[1]
    todo_list.append((importance, task))
    command = input()


def sort_key(element):
    return element[0]


sorted_tasks = sorted(todo_list, key=sort_key)

print(list(task[1] for task in sorted_tasks))

