using System;

namespace Dealership
{
    public class Car: IComparable<Car>
    {
        private const int GasTankMax = 300;
        private const int GasTankMin = 0;
        
        private string _model;
        private int _horsePower;
        private string _color;
        private double _fuel;

        public Car(
            string model,
            int horsePower,
            string color)
        {
            Model = model;
            HorsePower = horsePower;
            Color = color;
            
            Fuel = 0;
        }

        public string Refuel(double fuel)
        {
            double diff = Fuel + fuel;

            if (diff > GasTankMax)
            {
                Fuel = GasTankMax;
                return $"The car fuel should not be more than {GasTankMax}";
            }

            Fuel = diff;
            return $"Successful fill up! {Fuel} left.";
        }

        public string Drive(double fuel)
        {
            double diff = Fuel - fuel;

            if (diff < GasTankMin)
            {
                return $"The car needs more fuel. {Math.Abs(diff)} Needed!";
            }

            Fuel = diff;
            return $"Successful TEST DRIVE! {Fuel} left.";
        }

        public override string ToString()
        {
            return $"Model: {_model} / HorsePower: {_horsePower} / Color: {_color} ";
        }

        public string Model
        {
            get => _model;
            set => _model = value;
        }

        public int HorsePower
        {
            get => _horsePower;
            set
            {
                if (value < 0)
                {
                    throw new ArgumentException("The horse power should not be less than 0!");
                }

                _horsePower = value;
            }
        }

        public string Color
        {
            get => _color;
            set => _color = value;
        }

        public double Fuel
        {
            get => _fuel;
            set
            {
                if (value < 0)
                {
                    throw new ArgumentException("The fuel should not be less than 0!");
                }

                _fuel = value;
            }
        }
        
        public int CompareTo(Car other)
        {
            int result = _horsePower.CompareTo(other._horsePower);

            if (result == 0)
            {
                result = String.Compare(_model, other._model, StringComparison.Ordinal);
            }

            return result;
        }
    }
}