class Gym:
    def __init__(self):
        self.customers = list()
        self.trainers = list()
        self.equipment = list()
        self.plans = list()
        self.subscriptions = list()

    @staticmethod
    def find_object(subscription_id, objects_list):
        return [obj for obj in objects_list if obj.id == subscription_id][0]

    def does_customer_exist(self, customer):
        return customer in self.customers

    def does_trainer_exist(self, trainer):
        return trainer in self.trainers

    def does_equipment_exist(self, equipment):
        return equipment in self.equipment

    def does_plan_exist(self, plan):
        return plan in self.plans

    def does_subscription_exist(self, subscription):
        return subscription in self.subscriptions

    # ---------- Main ----------

    def add_customer(self, customer):
        if self.does_customer_exist(customer):
            return

        self.customers.append(customer)

    def add_trainer(self, trainer):
        if self.does_trainer_exist(trainer):
            return

        self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if self.does_equipment_exist(equipment):
            return

        self.equipment.append(equipment)

    def add_plan(self, plan):
        if self.does_plan_exist(plan):
            return

        self.plans.append(plan)

    def add_subscription(self, subscription):
        if self.does_subscription_exist(subscription):
            return

        self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        customer = Gym.find_object(subscription_id, self.customers)
        trainer = Gym.find_object(subscription_id, self.trainers)
        equipment = Gym.find_object(subscription_id, self.equipment)
        plan = Gym.find_object(subscription_id, self.plans)
        subscription = Gym.find_object(subscription_id, self.subscriptions)

        return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{plan}"
