class MovieWorld:
    CUSTOMERS_CAPACITY = 10
    DVDS_CAPACITY = 15

    def __init__(self, name: str):
        self.name = name
        self.customers = list()
        self.dvds = list()

    # ---------- Customer methods ----------

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMERS_CAPACITY

    @staticmethod
    def did_customer_already_rent_current_dvd(customer, dvd):
        return dvd in customer.rented_dvds

    @staticmethod
    def is_customer_under_the_age_restriction(customer, dvd):
        return customer.age < dvd.age_restriction

    def has_free_space_for_customer(self):
        return len(self.customers) < MovieWorld.customer_capacity()

    def find_customer(self, customer_id):
        return [customer for customer in self.customers if customer.id == customer_id][0]

    # ---------- DVD methods ----------

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVDS_CAPACITY

    @staticmethod
    def is_dvd_already_rented(dvd):
        return dvd.is_rented

    def has_free_space_for_dvd(self):
        return len(self.dvds) < MovieWorld.dvd_capacity()

    def find_dvd(self, dvd_id):
        return [dvd for dvd in self.dvds if dvd.id == dvd_id][0]

    # ---------- Others ----------

    def form_result(self):
        result = ""
        for customer in self.customers:
            result += f"{customer}\n"

        for dvd in self.dvds:
            result += f"{dvd}\n"

        return result

    # ---------- Main methods ----------

    def add_customer(self, customer):
        if not self.has_free_space_for_customer():
            return

        self.customers.append(customer)

    def add_dvd(self, dvd):
        if not self.has_free_space_for_dvd():
            return

        self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self.find_customer(customer_id)
        dvd = self.find_dvd(dvd_id)

        if MovieWorld.is_customer_under_the_age_restriction(customer, dvd):
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        if MovieWorld.did_customer_already_rent_current_dvd(customer, dvd):
            return f"{customer.name} has already rented {dvd.name}"

        if MovieWorld.is_dvd_already_rented(dvd):
            return "DVD is already rented"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.find_customer(customer_id)
        dvd = self.find_dvd(dvd_id)

        if not MovieWorld.did_customer_already_rent_current_dvd(customer, dvd):
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        return self.form_result()
