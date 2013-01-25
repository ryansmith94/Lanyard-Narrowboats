import classes
import unittest


class TestUser(unittest.TestCase):
    INITIAL_NAME = "John Smith"

    def setUp(self):
        self._user = classes.User(TestUser.INITIAL_NAME)

    def testName(self):
        USER = self._user

        return self.checkProperty(
            USER.getName,
            USER.setName,
            "Valid Name",
            "User Name Error",
            TestUser.INITIAL_NAME
        )

    def testAddress(self):
        USER = self._user

        return self.checkProperty(USER.getAddress,
            USER.setAddress,
            "1 Zero St, ZeroTown, CountyZero, ZZ0 0ZZ",
            "User Address Error",
            ""
        )

    def testPhone(self):
        USER = self._user

        return self.checkProperty(
            USER.getPhone,
            USER.setPhone,
            "00000000000",
            "User Phone Error",
            ""
        )

    def checkProperty(self, getFn, setFn, valid, msg, start):
        result = getFn()
        self.assertEqual(result, start, msg)

        result = self.erroneousTest(setFn, getFn, valid)
        self.assertEqual(result, 0, msg)

        return self

    def erroneousTest(self, setFn, getFn, valid):
        values = [valid, {}, 213, [], None, ""]
        for value in values:
            try:
                setFn(value)
            except:
                pass
        return values.index(getFn())


if __name__ == '__main__':
    unittest.main()
