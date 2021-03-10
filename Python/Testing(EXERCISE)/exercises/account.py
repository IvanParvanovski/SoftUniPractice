class Account(Exception):
    def __init__(self,
                 owner: str,
                 amount=0):

        self.owner = owner
        self.amount = amount
        self._transactions = list()

    @property
    def balance(self):
        return sum(self._transactions) + self.amount

    @staticmethod
    def __does_account_have_debt(account, amount_to_add):
        return amount_to_add + account.balance < 0

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if Account.__does_account_have_debt(account, amount_to_add):
            raise ValueError("sorry cannot go in debt!")

        account.add_transaction(amount_to_add)
        return f"New balance: {account.balance}"

    def add_transaction(self, amount):
        if isinstance(amount, int):
            self._transactions.append(amount)
            return

        raise ValueError("please use int for amount")

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        acc = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        acc._transactions = self._transactions + other._transactions
        return acc

    def __reversed__(self):
        return list(reversed(self._transactions))