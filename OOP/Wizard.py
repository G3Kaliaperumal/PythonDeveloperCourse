class User:
    def sign_in(self):
        print('logged in')


# Inheritance
class Wizard(User):
    def __init__(self, name, power):
        self._name = name
        self._power = power

    def showMyPower(self):
        print(f'I am {self._name} and my power is {self._power}')


hermoine = Wizard('Hermoine', 'lifting things using my mind')
hermoine.sign_in()
hermoine.showMyPower()
