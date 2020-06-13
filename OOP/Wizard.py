class User:
    def sign_in(self):
        print('logged in')


# Inheritance
class Wizard(User):
    def __init__(self, name, power):
        self._name = name
        self._power = power

    # Polymorphism
    def showMyPower(self):
        print(
            f'I am a wizard. My name is {self._name} and my power is {self._power}')


class Archer(User):
    def __init__(self, name, power):
        self._name = name
        self._power = power

    # Polymorphism
    def showMyPower(self):
        print(
            f'I am an archer. My name is {self._name} and my power is {self._power}')


hermoine = Wizard('Hermoine', 'lifting things using my mind')
hermoine.sign_in()
hermoine.showMyPower()

robin = Archer('Robin', 'a perfect shot. My aim never misses!')
robin.sign_in()
robin.showMyPower()
