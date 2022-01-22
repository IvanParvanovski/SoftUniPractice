using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace Dealership
{
    public class Warehouse<T>:
        IEnumerable<Car>
    {
        private List<Car> _cars = new List<Car>();
        private T id;
        private string _name;

        public Warehouse(string name, T id)
        {
            Name = name;
            this.id = id;
        }

        public string AddCar(Car car)
        {
            // Returns a message and adds a car to the warehouse.
            
            Console.ForegroundColor = ConsoleColor.DarkGreen;
            _cars.Add(car);
            return CenterText("Added successfully!");
        }

        public string RemoveCar(string searchedCar)
        {
            // Returns a message and removes a car from the warehouse.
            Car car = _cars.Find(x => x.Model == searchedCar);

            if (car == null)
            {
                Console.ForegroundColor = ConsoleColor.DarkRed;
                return CenterText("Car is not found!");
            }
            
            Console.ForegroundColor = ConsoleColor.DarkGreen;
            _cars.Remove(car);
            return CenterText("Removed successfully!");
        }
        
        public int GetAmount()
        {
            // Returns the amount of cars in the warehouse.
            
            return _cars.Count;
        }

        public string RepaintCar(string searchedCar, string newColor)
        {
            // If the searched car is found, hers color is changed.
            // In both occasions, a message is returned.
            
            Car car = _cars.Find(x => x.Model == searchedCar);

            if (car == null)
            {
                Console.ForegroundColor = ConsoleColor.DarkRed;
                return CenterText("Car is not found!");
            }

            Console.ForegroundColor = ConsoleColor.DarkGreen;
            car.Color = newColor;
            return CenterText("Repainted successfully!");
        }

        public string Tuning(string searchedCar, string part, int morePower)
        {
            // If the car is found, hers power is increased.
            // In both occasions, a message is returned.

            Car car = _cars.Find(x => x.Model == searchedCar);

            if (car == null)
            {
                Console.ForegroundColor = ConsoleColor.DarkRed;
                return CenterText("Car is not found!");
            }

            Console.ForegroundColor = ConsoleColor.DarkGreen;
            car.HorsePower += morePower;
            return CenterText($"Your car: {car.Model} has new part: {part} and {car.HorsePower}HP.");
        }

        public string TestDrive(string searchedCar)
        {
            // If the searched car is found and there is enough full,
            // a test drive is performed.
            
            Car car = _cars.Find(x => x.Model == searchedCar);

            if (car == null)
            {
                Console.ForegroundColor = ConsoleColor.DarkRed;
                return CenterText("Car is not found!");
            }

            Console.ForegroundColor = ConsoleColor.DarkMagenta;
            return CenterText(car.Drive(23));
        }

        public string RefuelCar(string searchedCar, double fuel)
        {
            // If the searched car is found, the gas tank if filled up
            // with the given amount of fuel.
            
            Car car = _cars.Find(x => x.Model == searchedCar);

            if (car == null)
            {
                Console.ForegroundColor = ConsoleColor.DarkRed;
                return CenterText("Car is not found!");
            }

            Console.ForegroundColor = ConsoleColor.DarkMagenta;
            return CenterText(car.Refuel(fuel));
        }
        
        public string CenterText(string text)
        {
            // Centers the text
            
            return String.Format("{0," + (Console.WindowWidth / 2 + text.Length / 2) + "}", text);
        }

        public string GetDisplayTable()
        {
            // Displays the information about the warehouse.
            
            string hyphen = $"|{string.Join("", Enumerable.Repeat("-", _name.Length * 5))}|";
            string name = $"<<<<<<< {_name} >>>>>>>";
            List<string> rows = new List<string>();
            rows.Add(CenterText(hyphen));
            rows.Add(CenterText(name));
            rows.Add(CenterText($"::: {id} :::"));
            rows.Add(CenterText(hyphen));
            
            rows.Add(CenterText(" {===== Cars =====} "));
            foreach (var car in _cars)
            {
                string carText = $" / {car} \\ ";
                rows.Add(CenterText(carText));    
            }
            
            rows.Add(CenterText(hyphen));
            
            Console.ForegroundColor = ConsoleColor.DarkBlue;
            return String.Join("\n", rows);
        }
        
        public string Name
        {
            get => _name;
            set => _name = value;
        }
        
        public IEnumerator<Car> GetEnumerator()
        {
            foreach (Car car in _cars.OrderBy(x => x))
            {
                yield return car;
            }
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
    }
}