using System;

namespace Ex9YardGreening
{
    class Program
    {
        static void Main(string[] args)
        {
            double squareFoots = double.Parse(Console.ReadLine());
            double pricePerSquareFoot = 7.61;
            double cost = squareFoots * pricePerSquareFoot;
            double discount = cost - 18.0 / 100 * cost;
            double finalPrice = cost - discount;

            Console.WriteLine(discount);
            Console.WriteLine(finalPrice);
            
        }
    }
}