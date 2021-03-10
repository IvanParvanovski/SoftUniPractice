class NameTooShortError(Exception):
    """ Raised when username is 4 symbols or less """
    def __init__(self, message="Name must be more than 4 characters"):
        self.message = message
        super().__init__(self.message)


class MustContainAtSymbolError(Exception):
    """ Raised when there isn't at symbol ("@") in the email """
    def __init__(self, message="Email must contain @"):
        self.message = message
        super().__init__(self.message)


class InvalidDomainError(Exception):
    """ Raised when there is invalid domain """
    def __init__(self, valid_domains, message=f"Domain must be one of the following: "):
        self.domains = valid_domains
        self.message = message + f".{', .'.join(self.domains)}"
        super().__init__(self.message)


def validate_name(email: str) -> None:
    username = email.split("@")[0]
    if len(username) <= 4:
        raise NameTooShortError()


def validate_at_symbol(email: str) -> None:
    if "@" not in email:
        raise MustContainAtSymbolError()


def validate_domain(email: str, domains: tuple) -> None:
    domain = email.split('.')[-1]
    if domain not in domains:
        raise InvalidDomainError(domains, "")


valid_domains = ("com",
                 "bg",
                 "org",
                 "net", )

while True:
    line = input()

    if line == "End":
        break

    validate_name(line)
    validate_at_symbol(line)
    validate_domain(line, valid_domains)

    print("Email is valid")
