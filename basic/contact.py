class Model:
    def __init__(self):
        self._name = ''
        self._phone = ''
        self._email = ''
        self._addr = ''

    def __str__(self) -> str:
        return self._name + ', ' + self._phone + ', ' + self._email + ', ' + self._addr

    @property
    def name(self) -> str: return self._name

    def name(self, name): self._name = name

    @property
    def phone(self) -> str: return self._phone

    @phone.setter
    def phone(self, phone): self._phone = phone

    @property
    def email(self) -> str : return self._phone

    @email.setter
    def email(self, email): self._email = email

    @property
    def addr(self) -> str : return self._addr

    @addr.setter
    def addr(self, addr): self._addr = addr


class Service:
    def __init__(self):
        self._contacts = []

    def add_contacts(self, payload):
        self._contacts.append(payload)

    def get_contact(self, payload):
        for i in self._contacts:
            if payload == i.name:
                return i

    def get_contacts(self):
        return self._contacts

    def del_contact(self, payload):
        for i in self._contacts:
            if payload == i.name:
                self._contacts.remove(i)


class Controller:

    def __init__(self):
        self._service = Service()

    def register(self, name, phone, email, addr):
        model = Model()
        model.name = name
        model.phone = phone
        model.email = email
        model.addr = addr
        self._service.add_contacts(model)

    def search(self, name):
        return self._service.get_contact(name)

    def list(self):
        return self._service.get_contacts()

    def remove(self, name):
        self._service.del_contact(name)


def print_menu():
    print('0. 종료')
    print('1. 연락처추가')
    print('2. 연락처 이름 검색')
    print('3. 연락처 목록 검색')
    print('4. 연락처 삭제')
    return input('Menu\n')

app = Controller()

while 1:
    menu = print_menu()
    if menu == '1':
        app.register(input('이름\n'),
                     input('전화번호\n'),
                     input('이메일\n'),
                     input('주소\n'))
    if menu == '2':
       print(''.join(app.search(input('이름\n'))))

    if menu == '3':
        app.list()

    if menu == '4':
        app.remove(input('이름\n'))
        app.list()

    elif menu == '0':
        break




