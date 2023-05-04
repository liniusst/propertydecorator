# pylint: disable= missing-docstring


class Temperature:
    def __init__(self, temp: float) -> None:
        self._temp: float = temp

    @property
    def celsius(self) -> float:
        return self._temp

    @celsius.setter
    def celsius(self, value: float) -> None:
        self._temp = value

    @property
    def fahrenheit(self) -> float:
        return round((self.celsius * 9 / 5) + 32, 2)


conversion = Temperature(15.3)
print(f"Celsius: {conversion.celsius}")
print(f"Fahrenheit: {conversion.fahrenheit}")
conversion.celsius = 22.3
print(f"Celsius after @setter: {conversion.celsius}")
print(f"Fahrenheit after @setter: {conversion.fahrenheit}")
