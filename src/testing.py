import classes
import unittest


class TestUser(unittest.TestCase):

    def setUp(self):
        self._user = classes.User("John Smith")

    def testName(self):
        USER = self._user
        GET_FN = USER.getName
        VALID = "1 Zero St, ZeroTown, CountyZero, ZZ0 0ZZ"
        MSG = "User Name Error"

        result = GET_FN()
        self.assertEqual(result, "John Smith", MSG)

        result = self.erroneousTest(USER.setName, GET_FN, VALID)
        self.assertEqual(result, 0, MSG)

        return self

    def testAddress(self):
        USER = self._user
        GET_FN = USER.getAddress
        VALID = "1 Zero St, ZeroTown, CountyZero, ZZ0 0ZZ"
        MSG = "User Address Error"

        result = GET_FN()
        self.assertEqual(result, "", MSG)

        result = self.erroneousTest(USER.setAddress, GET_FN, VALID)
        self.assertEqual(result, 0, MSG)

        return self

    def testPhone(self):
        USER = self._user
        GET_FN = USER.getPhone
        VALID = "00000000000"
        MSG = "User Phone Error"

        result = GET_FN()
        self.assertEqual(result, "", MSG)

        result = self.erroneousTest(USER.setPhone, GET_FN, VALID)
        self.assertEqual(result, 0, MSG)

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
