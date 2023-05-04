# pylint: disable= missing-docstring


class User:
    def __init__(self) -> None:
        self._password = None

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        if self.check_password(value) is not True:
            raise ValueError
        else:
            self._password = value

    def check_password(self, password: str) -> bool:
        upper: int = 0
        lower: int = 0
        digit: int = 0

        for letter in password:
            if letter.isupper():
                upper += 1
            if letter.islower():
                lower += 1
            if letter.isdigit():
                digit += 1

        if upper > 0 and lower > 0 and digit > 0 and len(password) > 8:
            return True


pwd = User()
try:
    pwd.password = "PPPPPPPPPPPP"
    print(pwd.password)
except ValueError:
    print("Password isn't strong")
