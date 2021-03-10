class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = list()

    def is_new_task_valid(self, new_task) -> bool:
        return new_task not in self.tasks

    def add_task(self, new_task) -> str:
        if not self.is_new_task_valid(new_task):
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        tasks_list = list(filter(lambda t: t.name == task_name, self.tasks))

        if not tasks_list:
            return f"Could not find task with the name {task_name}"

        task = tasks_list[0]
        task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self) -> str:
        completed_tasks = list(filter(lambda t: t.completed, self.tasks))

        for completed_task in completed_tasks:
            self.tasks.remove(completed_task)

        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self) -> str:
        result = f"Section {self.name}:\n"

        for t in self.tasks:
            result += f"{t.details()}\n"

        return result
