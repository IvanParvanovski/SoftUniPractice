class Customer:
    auto_increment = 1

    def __init__(
            self,
            name: str,
            address: str,
            email: str):

        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.auto_increment
        Customer.auto_increment += 1

    @staticmethod
    def get_next_id():
        return Customer.auto_increment

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
