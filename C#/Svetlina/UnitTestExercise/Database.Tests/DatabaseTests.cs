using NUnit.Framework;
using System;


namespace P01_Database
{
    public class DatabaseTests
    {
        private Database database;
        private readonly int[] initialData = new int[] { 1, 2 };

        [SetUp]
        public void Setup()
        {
            database = new Database(initialData);
        }

        [Test]
        public void TestCollectionLength()
        {
            int expectedLength = 2;

            Assert.That(database.Count, Is.EqualTo(expectedLength));
        }

        [Test]
        public void TestCorrectAddintToData()
        {
            int expectedCount = 3;

            database.Add(3);

            Assert.That(database.Count, Is.EqualTo(expectedCount));
        }

        [Test]
        public void TestCorrectThrowingExceptionAtAdding()
        {
            int magicNumber = 16;

            for (int i = database.Count; i < 16; i++)
            {
                database.Add(magicNumber);
            }

            Assert.Throws<InvalidOperationException>(() => database.Add(magicNumber));
        }

        [Test]
        public void TestCorrectRemoveFromCollection()
        {
            int expectedCount = 1;

            database.Remove();

            Assert.AreEqual(expectedCount, database.Count);
        }

        [Test]
        public void TestRemovingFromEmptyCollection()
        {
            for (int i = database.Count - 1; i >= 0; i--)
            {
                database.Remove();
            }

            Assert.Throws<InvalidOperationException>(() => database.Remove());
        }

        [Test]
        public void TestFetchDatabaseFunction()
        {
            int[] actualResult = database.Fetch();
            CollectionAssert.AreEqual(initialData, actualResult);
        }
    }
}