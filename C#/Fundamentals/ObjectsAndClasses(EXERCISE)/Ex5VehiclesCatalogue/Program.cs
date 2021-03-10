using System;
using System.Collections.Generic;

namespace Ex5VehiclesCatalogue
{
    class Program
    {
        static void Main(string[] args)
        {
            List<Car> cars = new List<Car>();
            List<Truck> trucks = new List<Truck>();
            
            while (true)
            {
                string input = Console.ReadLine();
                if (input == "End")
                    break;

                string[] data = input?.Split(' ');
                string type = data?[0];
                string model = data?[1];
                string color = data?[2];
                int horsePower  = int.Parse(data?[3] ?? string.Empty);
                
                switch (type)
                {
                    case "car":
                        Car car = new Car(model, color, horsePower);
                        cars.Add(car);
                        break;
                    case "truck":
                        Truck truck = new Truck(model, color, horsePower);
                        trucks.Add(truck);
                        break;
                }
            }

            while (true)
            {
                string input = Console.ReadLine();
                if (input == "Close the Catalogue")
                    break;

                string vehicleModel = input;
                bool isVehicleFound = false;
                
                foreach (Car car in cars)
                    if (car.Model == vehicleModel)
                    {
                        isVehicleFound = true;
                        Console.WriteLine(car);
                        break;
                    }
                
                if (isVehicleFound)
                    continue;

                foreach (Truck truck in trucks)
                    if (truck.Model == vehicleModel)
                    {
                        Console.WriteLine(truck);
                        break;
                    }
            }
            
            double carsAverageHorsePower = Math.Round(GetCarsAverageHorsePower(cars), 2);
            double trucksAverageHorsePower = Math.Round(GetTrucksAverageHorsePower(trucks), 2);

            Console.WriteLine($"Cars have average horsepower of: {(double.IsNaN(carsAverageHorsePower) ? 0 : carsAverageHorsePower):f2}.");
            Console.WriteLine($"Trucks have average horsepower of: {(double.IsNaN(trucksAverageHorsePower) ? 0 : trucksAverageHorsePower):f2}.");
        }

        private static double GetCarsAverageHorsePower(List<Car> cars)
        {
            int carsTotalHorsePower = 0;
            foreach (Car car in cars)
                carsTotalHorsePower += car.HorsePower;
            
            return carsTotalHorsePower * 1.0 / cars.Count;
        }

        private static double GetTrucksAverageHorsePower(List<Truck> trucks)
        {
            int trucksTotalHorsePower = 0;
            foreach (Truck truck in trucks)
                trucksTotalHorsePower += truck.HorsePower;
            
            return trucksTotalHorsePower * 1.0 / trucks.Count;
        }
    }
}