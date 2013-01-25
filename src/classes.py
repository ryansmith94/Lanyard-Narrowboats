class Lease(object):
    """Stores information about a Lease."""
    def __init__(self, customer, boat, start, end, package):
        """Creates a new lease instance."""
        self._customer = customer
        self._boat = boat
        self._start = start
        self._end = end
        self._package = package


class User(object):
    """Stores information about a user."""
    def __init__(self, name):
        self._name = name
        self._contact = {
            "address": "",
            "postcode": "",
            "phoneNumber": ""
        }

    def setName(self, name):
        self._name = name

    def setAddress(self, address, postcode):
        self._contact["address"] = address
        self._contact["postcode"] = postcode

    def setPhone(self, phoneNumber):
        self._contact["phoneNumber"] = phoneNumber

    def getName(self):
        return self._name

    def getAddress(self):
        return self._contact["address"] + self._contact["postcode"]

    def getPhone(self):
        return self._phone


class Customer(User):
    """Stores information about a customer."""
    def __init__(self, name):
        super(Customer, self).__init__(name)
        self._boats = []

    def addBoat(self, boat):
        self._boats.append(boat)

    def removeBoat(self, boat):
        boats = self._boats
        boats.pop(boats.index(boat))

    def getBoats(self):
        return self._boats


class Boat(object):
    """Stores information about a boat."""
    def __init__(self, name, description):
        self._name = name
        self._description = description

    def setName(self, name):
        self._name = name

    def setDescription(self, description):
        self._description = description

    def getName(self):
        return self._name

    def getDescription(self):
        return self._description
