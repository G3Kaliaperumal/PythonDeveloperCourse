class Travel():
    pass


class DomesticTravel(Travel):
    def __init__(self, place, mode_of_transport):
        self._place = place
        self._mode_of_transport = mode_of_transport

    def fetchTravelDetails(self):
        print(
            f'Domestic Travel to {self._place} using {self._mode_of_transport}')


class InternationalTravel(Travel):
    def __init__(self, place, has_passport):
        self._place = place
        self._has_passport = has_passport

    def fetchTravelDetails(self):
        print(
            f'International Travel to {self._place}. Do I have a passport for that? {self._has_passport}')


class Both(DomesticTravel, InternationalTravel):
    def __init__(self, places, mode_of_transport, has_passport):
        DomesticTravel.__init__(self, places[0], mode_of_transport)
        InternationalTravel.__init__(self, places[1], has_passport)

    def fetchTravelDetails(self):
        DomesticTravel.fetchTravelDetails(self)
        InternationalTravel.fetchTravelDetails(self)


# Observe what happens when the variable name are equal in both classes
both = Both(['Jaipur', 'Canada'], 'Train', 'Yes')
both.fetchTravelDetails()
print(Both.mro())
