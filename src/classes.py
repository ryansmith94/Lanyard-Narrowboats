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
        self.setName(name)
        self._contact = {
            "address": "",
            "phoneNumber": ""
        }

    def setName(self, name):
        self._name = validString(name, 5, 250)
        return self

    def setAddress(self, address):
        self._contact["address"] = validString(address, 5, 250)
        return self

    def setPhone(self, phoneNumber):
        self._contact["phoneNumber"] = validString(phoneNumber, 10, 20)
        return self

    def getName(self):
        return self._name

    def getAddress(self):
        return self._contact["address"]

    def getPhone(self):
        return self._contact["phoneNumber"]


class Customer(User):
    """Stores information about a customer."""
    def __init__(self, name):
        super(Customer, self).__init__(name)
        self._boats = []

    def addBoat(self, boat):
        self._boats.append(boat)
        return self

    def removeBoat(self, boat):
        boats = self._boats
        boats.pop(boats.index(boat))
        return self

    def getBoats(self):
        return self._boats


class Boat(object):
    """Stores information about a boat."""
    def __init__(self, name, description):
        self._name = name
        self._description = description
        self._owners = []

    def setName(self, name):
        self._name = name
        return self

    def setDescription(self, description):
        self._description = description
        return self

    def getName(self):
        return self._name

    def getDescription(self):
        return self._description

    def addOwner(self, owner):
        self._owners.append(owner)
        return self

    def removeOwner(self, owner):
        self._owners.pop(self._owners.index(owner))
        return self

    def getOwners(self):
        return self._owners


def validString(value, minLength, maxLength):
    if (isinstance(value, str) == True) and (minLength < len(value) < maxLength):
        return value
    else:
        raise Exception("Value must be a string between {0} and {1} characters (exclusive).".format(minLength, maxLength))
