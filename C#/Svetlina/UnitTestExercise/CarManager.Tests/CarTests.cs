using NUnit.Framework;
using System;

namespace P03_CarManager
{
    public class CarTests
    {
        private Car vehicle;

        [SetUp]
        public void Setup()
        {
            vehicle = new Car("Audi", "A4", 15, 300);
        }

        [Test]
        public void TestIfConstructorWorksCorrectly()
        {
            Assert.IsNotNull(vehicle);
        }
        [Test]
        public void TestRefuelWithZero()
        {

            Assert.Throws<ArgumentException>(
                () => { vehicle.Refuel(0); },
                "Make cannot be null or empty!"
            );
        }

        [Test]
        public void TestMakeValidation()
        {
            Assert.Throws<ArgumentException>(
                () => { Car newCar = new Car(null, "A4", 15, 300); },
                "Make cannot be null or empty!"
            );
        }

        [Test]
        public void TestModelValidation()
        {
            Assert.Throws<ArgumentException>(
                () => { Car newCar = new Car("Audi", null, 15, 300); },
                "Model cannot be null or empty!"
            );
        }

        [Test]
        public void TestFuelConsumptionValidation()
        {
            Assert.Throws<ArgumentException>(
                () => { Car newCar = new Car("Audi", "A4", -3, 300); },
                "Fuel consumption cannot be zero or negative!"
            );
        }

        [Test]
        public void TestFuelCapacityValidation()
        {
            Assert.Throws<ArgumentException>(
                () => { Car newCar = new Car("Audi", "A4", 15, 0); },
                "Fuel capacity cannot be zero or negative!"
            );
        }

        [Test]
        public void TestFuelAmount()
        {
            Assert.That(0, Is.EqualTo(vehicle.FuelAmount));
        }

        [Test]
        public void TestRefuelingCorrectly()
        {
            vehicle.Refuel(15);
            int expectedFuel = 15;

            Assert.That(expectedFuel, Is.EqualTo(vehicle.FuelAmount));
        }

        [Test]
        public void TestIfFuelToRefuelIsNegativeNumber()
        {
            Assert.Throws<ArgumentException>(
                () =>  { vehicle.Refuel(-3); },
                "Fuel amount cannot be zero or negative!"
            );
        }

        [Test]
        public void TestIfRefuelMoreThanCapacity()
        {
            int expectedFuel = 300;

            vehicle.Refuel(350);

            Assert.That(expectedFuel, Is.EqualTo(vehicle.FuelAmount));
        }

        [Test]
        public void TestDrivingCorrectly()
        {
            double expectedFuel = 8.5;

            vehicle.Refuel(10);
            vehicle.Drive(10);

            Assert.AreEqual(expectedFuel, vehicle.FuelAmount);
        }

        [Test]
        public void TestDrivingTooMuchDistance()
        {
            vehicle.Refuel(1);

            Assert.Throws<InvalidOperationException>(
                () => { vehicle.Drive(10); },
                "You don't have enough fuel to drive!"
            );
        }
    }
}