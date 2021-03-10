import unittest

from exercises.groups import Person, Group


class TestPerson(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        name1 = 'Zachary'
        surname1 = 'Efron'

        name2 = 'Will'
        surname2 = 'Smith'

        cls.p1 = Person(name1, surname1)
        cls.p2 = Person(name2, surname2)

    def test_personInit_shouldIdIncrease(self):
        self.assertEqual(self.p1.id, self.p1.id)
        self.assertEqual(self.p2.id, self.p2.id)

    def test_personAdd_shouldCreateNewObject(self):
        expected_name = 'Zachary'
        expected_surname = 'Smith'

        p3 = self.p1 + self.p2

        self.assertEqual(expected_name, p3.name)
        self.assertEqual(expected_surname, p3.surname)

    def test_personRepr_shouldReturnCorrectMessage(self):
        msg1 = f'Person {self.p1.id}: Zachary Efron'
        msg2 = f'Person {self.p2.id}: Will Smith'

        self.assertEqual(repr(self.p1), msg1)
        self.assertEqual(repr(self.p2), msg2)


class TestGroup(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.p4 = Person('Ivan', 'Parvanovski')
        cls.p5 = Person('Teodor', 'Draizer')

        group_name1 = 'Galaxy'
        group_members1 = [cls.p4, cls.p5]

        cls.g1 = Group(group_name1, group_members1)

    def test_groupAdd(self):

        # Arrange
        p6 = Person('Margot', 'Robbie')
        p7 = Person('Kevin', 'Hart')

        group_name2 = 'Stars'
        group_members2 = [p6, p7]

        g2 = Group(group_name2, group_members2)

        expected_name = 'Galaxy'
        expected_people = [self.p4, self.p5, p6, p7]

        # Act
        g3 = self.g1 + g2

        # Assert
        self.assertEqual(expected_name, g3.name)
        self.assertEqual(expected_people, g3.people)

    def test_groupLen(self):
        expected_len = 2
        actual_len = len(self.g1)

        self.assertEqual(expected_len, actual_len)

    def test_groupGetItem(self):
        expected_msg = repr('Person 0: Ivan Parvanovski')
        actual_msg = repr(self.g1[0])

        self.assertEqual(expected_msg, actual_msg)

    def test_groupStr(self):
        expected_msg = 'Group Galaxy with members Ivan Parvanovski, Teodor Draizer'
        self.assertEqual(expected_msg, str(self.g1))


if __name__ == '__main__':
    unittest.main()
