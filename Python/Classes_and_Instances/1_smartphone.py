class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = list()
        self.is_on = False

    def does_phone_have_free_memory(self, app_memory):
        return app_memory <= self.memory

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        if not self.is_on:
            return f"Turn on your phone to install {app}"

        if not self.does_phone_have_free_memory(app_memory):
            return f"Not enough memory to install {app}"

        self.apps.append(app)
        self.memory -= app_memory
        return f"Installing {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
