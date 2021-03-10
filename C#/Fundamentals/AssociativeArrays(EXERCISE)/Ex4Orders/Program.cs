using System;
using System.Collections.Generic;

namespace Ex4Orders
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, double[]> products = new Dictionary<string, double[]>();

            while (true)
            {
                string userInput = Console.ReadLine();
                if (userInput == "buy")
                    break;

                string[] userData = userInput.Split();
                string product = userData[0];
                double price = Convert.ToDouble(userData[1]);
                int quantity = Convert.ToInt32(userData[2]);
                double currentQuantity;

                try
                {
                    currentQuantity = products[product][1];
                }
                catch
                {
                    currentQuantity = 0;
                }


                products[product] = new double[] { price, quantity + currentQuantity };

                }
            foreach (var item in products)
                Console.WriteLine($"{item.Key} -> {item.Value[0] * item.Value[1]:f2}");
        }
    }
}
