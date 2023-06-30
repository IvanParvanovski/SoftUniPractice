using NUnit.Framework;
using System;

namespace P02_ExtendedDatabase
{
    public class ExtendedDatabaseTests
    {
        private ExtendedDatabase database;

        [SetUp]
        public void Setup()
        {
            database = new ExtendedDatabase();
        }

        [Test]
        public void TestAddUserWithExistingUsername() 
        {
            var person1 = new Person(1, "Random");
            var person2 = new Person(2, "Random");

            database.Add(person1);
            Assert.That(() =>
            {
                database.Add(person2);
            }, Throws.InstanceOf<InvalidOperationException>());
        }

        [Test]
        public void TestAddUserWithExistingId()
        {
            var person1 = new Person(1, "Random1");
            var person2 = new Person(1, "Random2");

            database.Add(person1);
            Assert.That(() =>
            {
                database.Add(person2);
            }, Throws.InstanceOf<InvalidOperationException>());
        }

        [Test]
        public void TestAddUsers()
        {
            var person1 = new Person(1, "Random1");
            var person2 = new Person(2, "Random2");
            var person3 = new Person(3, "Random3");

            database.Add(person1);
            database.Add(person2);
            database.Add(person3);

            Assert.That(database.Count, Is.EqualTo(3));
        }

        [Test]
        public void TestRemoveWhenZero()
        {
            Assert.That(() =>
            {
                database.Remove();
            }, Throws.InstanceOf<InvalidOperationException>());
        }

        [Test]
        public void TestRemoveWhenThereArePeople()
        {
            var person1 = new Person(1, "Random1");
            var person2 = new Person(2, "Random2");

            database.Add(person1);
            database.Add(person2);
            Assert.That(database.Count, Is.EqualTo(2));


            database.Remove();
            Assert.That(database.Count, Is.EqualTo(1));
        }

        [Test]
        public void TestFindByUsernameWhenGivenEmptyString()
        {
            Assert.Throws<ArgumentNullException>(
                () => database.FindByUsername(""),
                "Username parameter is null!"
            );
        }

        [Test]
        public void TestFindByUsernameWhenNoSuchUser()
        {
            Assert.Throws<InvalidOperationException>(
                () => database.FindByUsername("Random"),
                "No user is present by this username!"
            );
        }

        [Test]
        public void TestFindByUsernameWhenCaseSensitive()
        {
            var person1 = new Person(1, "random");
            database.Add(person1);

            Assert.Throws<InvalidOperationException>(
                () => database.FindByUsername("RANDOM"),
                "No user is present by this username!"
            );
        }

        [Test]
        public void TestFindByUsernameWhenUserExists()
        {
            var person1 = new Person(1, "Random");

            database.Add(person1);
            var result = database.FindByUsername("Random");

            Assert.That(result, Is.EqualTo(person1));
        }

        [Test]
        public void TestFindByIdWhenNegativeId()
        {
            Assert.Throws<ArgumentOutOfRangeException>(
                () => database.FindById(-1),
                "Id should be a positive number!"
            );
        }

        [Test]
        public void TestFindByIdWhenInvalidId()
        {
            var person1 = new Person(1, "Random");
            database.Add(person1);

            Assert.Throws<InvalidOperationException>(
                () => database.FindById(10000)
            );
        }

        [Test]
        public void TestFindByIdWhenValidId()
        {
            var person1 = new Person(1, "Random");

            database.Add(person1);
            var result = database.FindById(1);

            Assert.That(result, Is.EqualTo(person1));
        }
    }
}