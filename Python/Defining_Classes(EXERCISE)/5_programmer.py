class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def does_programmer_has_skills(self, needed_skills: int) -> bool:
        return self.skills >= needed_skills

    def does_programmer_know_language(self, language: str) -> bool:
        return language == self.language

    def watch_course(self, course_name: str, language: str, skills_earned: int) -> str:

        if not self.does_programmer_know_language(language):
            return f"{self.name} does not know {language}"

        self.skills += skills_earned
        return f"{self.name} watched {course_name}"

    def change_language(self, new_language: str, skills_needed: int) -> str:

        if not self.does_programmer_has_skills(skills_needed):
            return f"{self.name} needs {skills_needed - self.skills} more skills"

        if self.does_programmer_know_language(new_language):
            return f"{self.name} already knows {new_language}"

        message = f"{self.name} switched from {self.language} to {new_language}"
        self.language = new_language
        return message


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))

"""
O U T P U T

John does not know Python
John already knows Java
John needs 50 more skills
John watched Java: zero to hero
John switched from Java to Python
John watched Python Masterclass

"""