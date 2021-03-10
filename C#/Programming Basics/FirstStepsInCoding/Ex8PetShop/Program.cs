using System;

namespace Ex8PetShop
{
    class Program
    {
        static void Main(string[] args)
        {
            int dogsCount = int.Parse(Console.ReadLine());
            int otherAnimalsCount = int.Parse(Console.ReadLine());
            double cost = dogsCount * 2.50 + otherAnimalsCount * 4;
            Console.WriteLine($"{cost} lv.");
        }
    }
}
