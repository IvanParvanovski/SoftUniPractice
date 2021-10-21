using System;

namespace Ex1
{
    class Program
    {
        static void Main(string[] args)
        {
            Car car = new Car();
            
            car.Make = "VW";
            car.Model = "MK3";
            car.Year = 1992;
            
            Console.WriteLine($"Make: {car.Make}\n" +
                              $"Model: {car.Model}\n" +
                              $"Year: {car.Year}");
        }
    }
}