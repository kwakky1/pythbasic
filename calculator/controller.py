from calculator.model import Model
from calculator.service import Service


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
