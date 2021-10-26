using System;
using System.Collections.Generic;

namespace Ex6SpeedRacing
{
    class Program
    {
        static void Main(string[] args)
        {
            List<Car> cars = new List<Car>();
            int n = int.Parse(Console.ReadLine()!);
            
            for (int i = 0; i < n; i++)
            {
                string[] cardData = Console.ReadLine()!.Split();
                
                cars.Add(new Car(
                    cardData[0],
                    double.Parse(cardData[1]), 
                    double.Parse(cardData[2]))
                );
            }
            
            while (true)
            {
                string command = Console.ReadLine();

                if (command == "End")
                {
                    break;
                }
                
                string[] commandData = command!.Split();
                
                string carModel = commandData[1];
                int distance = int.Parse(commandData[2]);
                
                Car searchedCar = getCar(cars, carModel);
                searchedCar.Drive(distance);
            }
            
            for (int i = 0; i < cars.Count; i++)
            {
                Console.WriteLine(cars[i].ToString());
            }
        }
        public static Car getCar(List<Car> cars, string searchedModel)
        {
            for (int i = 0; i < cars.Count; i++)
            {
                if (cars[i].Model == searchedModel)
                {
                    return cars[i];
                }
            }

            return new Car();
        }
    }
}