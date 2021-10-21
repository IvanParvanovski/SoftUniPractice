using System;

namespace Ex2CarAddMoreMembers
{
    public class Car
    {
        private string _make;
        private string _model;
        private int _year;
        private double _fuelQuantity;
        private double _fuelConsumption;

        public Car()
        {
            
        }
        
        public string Make
        {
            get => _make;
            set => _make = value;
        }

        public string Model
        {
            get => _model;
            set => _model = value;
        }

        public int Year
        {
            get => _year;
            set => _year = value;
        }

        public double FuelQuantity
        {
            get => _fuelQuantity;
            set => _fuelQuantity = value;
        }

        public double FuelConsumption
        {
            get => _fuelConsumption;
            set => _fuelConsumption = value;
        }

        public void Drive(double distance)
        {
            double neededFuel = distance * _fuelConsumption ;
            double balance = _fuelQuantity - neededFuel;
            
            if (balance > 0)
            {
                _fuelQuantity -= neededFuel;
            }
            else
            {
                Console.WriteLine("Not enough fuel to perform this trip!");
            }
        }

        public string WhoAmI()
        {
            return $"Make: {this.Make}\n" +
                   $"Model: {this.Model}\n" +
                   $"Year: {this.Year}\n" +
                   $"Fuel: {this.FuelQuantity:F2}L";
        }
    }
}