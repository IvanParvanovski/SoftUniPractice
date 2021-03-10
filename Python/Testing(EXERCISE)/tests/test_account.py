import unittest

from exercises.account import Account


class TestAccount(unittest.TestCase):
    def setUp(self) -> None:
        self.acc = Account('Ivan')

    def test_accountBalance_shouldReturnTransactionPlusAmount(self):
        self.acc.add_transaction(5)

        expected = 5
        actual = self.acc.balance

        self.assertEqual(expected, actual)

    def test_accountValidateTransaction_whenAccountHasDebt_shouldRaiseError(self):
        with self.assertRaises(Exception) as context:
            acc2 = Account('Nikolai')
            self.acc.validate_transaction(acc2, -5)

        self.assertIsNotNone(context.exception)

    def test_accountValidateTransaction_whenAccountDoesNotHaveDebt_shouldMakeTransaction(self):
        acc2 = Account('Nikolai')
        money_to_transfer = 5

        self.acc.validate_transaction(acc2, money_to_transfer)

        expected = 'New balance: 10'
        actual = self.acc.validate_transaction(acc2, money_to_transfer)
        self.assertEqual(expected, actual)

    def test_accountAddTransaction_whenAmountIsNotInt_shouldRaiseException(self):
        with self.assertRaises(Exception) as context:
            self.acc.add_transaction('10')

        self.assertIsNotNone(context.exception)

    def test_accountAddTransaction_whenAmountIsInt_shouldBeAdded(self):
        self.acc.add_transaction(5)

        expected = [5]
        actual = self.acc._transactions

        self.assertListEqual(expected, actual)

    def test_accountStr_shouldReturnCorrectMessage(self):
        expected_msg = 'Account of Ivan with starting amount: 0'
        actual = str(self.acc)

        self.assertEqual(expected_msg, actual)

    def test_accountRepr_shouldReturnCorrectMessage(self):
        expected_msg = 'Account(Ivan, 0)'
        actual = repr(self.acc)

        self.assertEqual(expected_msg, actual)

    def test_accountLen_shouldReturnTransactionsLength(self):
        self.acc.add_transaction(5)
        self.acc.add_transaction(10)

        expected = 2
        actual = len(self.acc)

        self.assertEqual(expected, actual)

    def test_accountGetItem_whenIndexIsValid_shouldReturnTransaction(self):
        self.acc.add_transaction(5)
        self.acc.add_transaction(10)

        expected = 10
        actual = self.acc[1]

        self.assertEqual(expected, actual)

    def test_accountGetItem_whenIndexIsInvalid_shouldReturnTransaction(self):
        with self.assertRaises(Exception) as context:
            actual = self.acc[100]

        self.assertIsNotNone(context.exception)

    def test_accountGraterThan_shouldReturnTurn(self):
        acc2 = Account('Nikolai')
        acc2.add_transaction(5)

        result = acc2 > self.acc
        self.assertTrue(result)

    def test_accountGraterThanOrEqual_shouldReturnTurn(self):
        acc2 = Account('Nikolai')
        acc2.add_transaction(5)

        self.acc.add_transaction(5)

        result = acc2 >= self.acc
        self.assertTrue(result)

    def test_accountLessThan_shouldReturnTurn(self):
        acc2 = Account('Nikolai')
        acc2.add_transaction(5)

        result = self.acc < acc2
        self.assertTrue(result)

    def test_accountLessThanOrEqual_shouldReturnTrue(self):
        acc2 = Account('Nikolai')
        acc2.add_transaction(5)

        self.acc.add_transaction(5)

        result = self.acc <= acc2
        self.assertTrue(result)

    def test_accountEqual_shouldReturnTrue(self):
        acc2 = Account('Nikolai')
        result = self.acc == acc2

        self.assertEqual(True, result)

    def test_accountNotEqual_shouldReturnTrue(self):
        acc2 = Account('Nikolai')
        acc2.add_transaction(2)

        result = self.acc != acc2

        self.assertTrue(result)

    def test_accountAdd_shouldReturnTrue(self):
        acc2 = Account('Nikolai')
        self.acc.add_transaction(10)
        acc2.add_transaction(5)

        acc3 = self.acc + acc2

        expected_name = 'Ivan&Nikolai'
        expected_transactions = [10, 5]
        expected_amount = 0

        actual_name = acc3.owner
        actual_transactions = acc3._transactions
        actual_amount = acc3.amount

        self.assertEqual(expected_name, actual_name)
        self.assertEqual(expected_transactions, actual_transactions)
        self.assertEqual(expected_amount, actual_amount)

    def test_accountReversed_shouldReturnReversedTransactions(self):
        self.acc.add_transaction(5)
        self.acc.add_transaction(10)
        self.acc.add_transaction(15)

        expected = [15, 10, 5]
        actual = reversed(self.acc)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
