using System;

namespace ExTest
{
    public class Car : IComparable<Car>
    {

        private int _year;
        public Car(string model, int year)
        {
            this.Model = model;
            this.Year = year;
        }
        
        public string Model { get; set; }
        public int Year
        {
            get => _year;
            set
            {
                if (value < 2000)
                {
                    throw new Exception("Should be more than 2000");
                }

                _year = value;
            }
        }

        public int CompareTo(Car other)
        {
            int result = this.Year.CompareTo(other.Year);

            if (result == 0)
            {
                result = this.Model.CompareTo(other.Model);
            }
            
            return result;
        }

        public override string ToString()
        {
            return $"{Model} -> {Year}";
        }
    }
}