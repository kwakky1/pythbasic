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


class Service:
    def __init__(self, payload):
        self._num1 = payload.num1
        self._num2 = payload.num2

    def plus(self):
        return self._num1 + self._num2

    def minus(self):
        return self._num1 - self._num2

    def multi(self):
        return self._num1 * self._num2

    def divide(self):
        return self._num1 / self._num2


class Controller:
    def calculator(self, num1, num2, operator):
        model = Model()
        model.num1 = num1
        model.num2 = num2
        model.operator = operator
        service = Service(model)

        if operator == '+':
            result = service.plus()
        if operator == '-':
            result = service.minus()
        if operator == '*':
            result = service.multi()
        if operator == '/':
            result = service.divide()
        return result


def print_menu():
    print('0. Exit')
    print('1. Calculator')
    return input('Menu\n')


while 1:
    menu = print_menu()
    if menu == '0': break
    if menu == '1':
        app = Controller()
        print('계산기 작동')
        num1 = int(input('첫번째 수\n'))
        operator = input('연산자\n')
        num2 = int(input('두번째 수\n'))

        result = app.calculator(num1, num2, operator)
        print('결과: %d' % result)
