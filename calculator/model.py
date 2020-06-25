class Model:
    def __init__(self):
        self._num1 = 0
        self._num2 = 0
        self._operator = ''

    @property
    def num1(self) -> int: return self._num1

    @num1.setter
    def num1(self, num1): self._num1 = num1

    @property
    def num2(self) -> int: return self._num2

    @num2.setter
    def num2(self, num2): self._num2 = num2

    @property
    def operator(self) -> str: return self._operator

    @operator.setter
    def operator(self, operator): self._operator = operator
