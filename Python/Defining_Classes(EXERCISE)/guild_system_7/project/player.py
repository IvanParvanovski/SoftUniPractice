class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = dict()
        self.guild = "Unaffiliated"

    def does_skill_exist(self, skill_name):
        return skill_name in self.skills

    def add_skill(self, skill_name, mana_cost):
        if self.does_skill_exist(skill_name):
            return "Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        result = f"Name: {self.name}\n"
        result += f"Guild: {self.guild}\n"
        result += f"HP: {self.hp}\n"
        result += f"MP: {self.mp}\n"

        for skill in self.skills:
            result += f"==={skill} - {self.skills[skill]}\n"

        return result
