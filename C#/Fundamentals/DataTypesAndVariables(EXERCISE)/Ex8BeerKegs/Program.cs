using System;

namespace Ex8BeerKegs
{
    class Program
    {
        static void Main(string[] args)
        {
            string biggestKeg = "";
            double biggestKegValue = 0;

            int num = int.Parse(Console.ReadLine());

            for (int i = 0; i < num; i++)
            {
                string currentKegName = Console.ReadLine();
                decimal currentRadius = decimal.Parse(Console.ReadLine());
                int currentHeight = int.Parse(Console.ReadLine());

                double currentKegValue = Math.PI * (double)Decimal.Multiply(currentRadius, currentRadius) * currentHeight;
                if (currentKegValue > biggestKegValue)
                {  
                    biggestKeg = currentKegName;
                    biggestKegValue = currentKegValue;
                }
            }

            Console.WriteLine(biggestKeg);
        }
    }
}
