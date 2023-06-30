using Collections;
using NUnit.Framework;
using System;
using System.Linq;

namespace CollectionTests
{
    public class Tests
    {
        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void Test1()
        {

            Assert.Pass();
        }

        [Test]
        public void Test_Collection_EmptyConstructor() 
        {
            // Arrange

            var nums = new Collection<int>();

            // Assert

            Assert.That(nums.ToString(), Is.EqualTo("[]"));
        }

        [Test]
        public void Test_Collection_ConstructorSingleItem() 
        {
            var nums = new Collection<int>(5);

            Assert.That(nums.ToString(), Is.EqualTo("[5]"));
        }

        [Test]
        public void Test_Collection_ConstructorMultipleItems() 
        {
            var nums = new Collection<int>(5, 10, 15);

            Assert.That(nums.ToString(), Is.EqualTo("[5, 10, 15]"));
        }

        [Test]
        public void Test_Collection_Add()
        {
            // Arrange

            var nums = new Collection<int>();

            // Act

            nums.Add(5);

            nums.Add(6);

            // Assert

            // Assert.Equals(nums.ToString(), Is.EqualTo("[5, 6]"));
        }

        [Test]
        public void Test_Collection_AddWithGrow() 
        {
            var nums = new Collection<int>();

            int oldCapacity = nums.Capacity;

            var newNums = Enumerable.Range(1000, 2000).ToArray();

            nums.AddRange(newNums);

            string expectedNums = "[" + string.Join(", ", newNums) + "]";

            Assert.That(nums.ToString(), Is.EqualTo(expectedNums));

            Assert.That(nums.Capacity,
            Is.GreaterThanOrEqualTo(oldCapacity));

            Assert.That(nums.Capacity, Is.GreaterThanOrEqualTo(nums.Count));
        }

        public void Test_Collection_AddRange() 
        {
        
        
        }

        [Test]
        public void Test_Collection_GetByIndex() 
        {
            // Arrange

            var names = new Collection<string>("Peter", "Maria");

            // Act

            var item0 = names[0];

            var item1 = names[1];

            // Assert

            Assert.That(item0, Is.EqualTo("Peter"));

            Assert.That(item1, Is.EqualTo("Maria"));
        }


        [Test]
        public void Test_Collection_GetByInvalidIndex() 
        {
            var names = new Collection<string>("Bob", "Joe");

            Assert.That(() => { var name = names[-1]; },

            Throws.InstanceOf<ArgumentOutOfRangeException>());

            Assert.That(() => { var name = names[2]; },

            Throws.InstanceOf<ArgumentOutOfRangeException>());

            Assert.That(() => { var name = names[500]; },

            Throws.InstanceOf<ArgumentOutOfRangeException>());

            Assert.That(names.ToString(), Is.EqualTo("[Bob, Joe]"));
        }

        public void Test_Collection_SetByIndex() 
        { 
        }

        public void Test_Collection_SetByInvalidIndex() 
        { }

        public void Test_Collection_AddRangeWithGrow() { }

        public void Test_Collection_InsertAtStart() {  }

        public void Test_Collection_InsertAtEnd() {  }

        public void Test_Collection_InsertAtMiddle() {  }

        public void Test_Collection_InsertAtWithGrow() {  }

        public void Test_Collection_InsertAtInvalidIndex() {  }

        public void Test_Collection_ExchangeMiddle() {  }

        public void Test_Collection_ExchangeFirstLast() {  }

        public void Test_Collection_ExchangeInvalidIndexes() {  }

        public void Test_Collection_RemoveAtStart() {  }

        public void Test_Collection_RemoveAtEnd() {  }

        public void Test_Collection_RemoveAtMiddle() {  }

        public void Test_Collection_RemoveAtInvalidIndex() {  }

        public void Test_Collection_RemoveAll() {  }

        public void Test_Collection_Clear() {  }

        public void Test_Collection_CountAndCapacity() {  }

        public void Test_Collection_ToStringEmpty() {  }

        public void Test_Collection_ToStringSingle() {  }

        public void Test_Collection_ToStringMultiple() { }


        [Test]
        public void Test_Collection_ToStringNestedCollections() 
        {
            var names = new Collection<string>("Teddy", "Gerry");

            var nums = new Collection<int>(10, 20);

            var dates = new Collection<DateTime>();

            var nested = new Collection<object>(names, nums, dates);

            string nestedToString = nested.ToString();

            Assert.That(nestedToString,

            Is.EqualTo("[[Teddy, Gerry], [10, 20], []]"));
        }

        [Test]

        public void Test_Collection_1MillionItems() 
        {
            const int itemsCount = 1000000;

            var nums = new Collection<int>();

            nums.AddRange(Enumerable.Range(1, itemsCount).ToArray());

            Assert.That(nums.Count == itemsCount);

            Assert.That(nums.Capacity >= nums.Count);

            for (int i = itemsCount - 1; i >= 0; i--)

                nums.RemoveAt(i);

            Assert.That(nums.ToString() == "[]");

            Assert.That(nums.Capacity >= nums.Count);
        }
    }
}