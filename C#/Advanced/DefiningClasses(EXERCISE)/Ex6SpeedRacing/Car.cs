using System;
using System.Net.NetworkInformation;
using System.Xml.Schema;

namespace Ex6SpeedRacing
{
    public class Car
    {
        private string _model;
        private double _fuelAmount;
        private double _fuelConsumption;
        private int _travelledDistance;
        
        public Car() {}
        public Car(string model, double fuelAmount, double fuelConsumption)
        {
            this.Model = model;
            this.FuelAmount = fuelAmount;
            this.FuelConsumption = fuelConsumption;
            this.TravelledDistance = 0;
        }
        public string Model
        {
            get { return _model; }
            set { _model = value; }
        }
        public int TravelledDistance
        {
            get { return _travelledDistance; }
            set { _travelledDistance = value; }
        }
        public double FuelConsumption
        {
            get { return _fuelConsumption; }
            set { _fuelConsumption = value; }
        }
        public double FuelAmount
        {
            get { return _fuelAmount; }
            set { _fuelAmount = value; }
        }
        
        public void Drive(int distance)
        {
            double neededFuel = distance * 1.0 * _fuelConsumption;
            if (neededFuel <= _fuelAmount)
            {
                FuelAmount -=neededFuel;
                _travelledDistance += distance;
            }
            else
            {
                Console.WriteLine("Insufficient fuel for the drive");
            }
        }
        
        public override string ToString()
        {
            return $"{_model} {_fuelAmount:f2} {_travelledDistance}";
        }
    }
}