using System;

namespace Ex5PrintPartOfTheASCIITable
{
    class Program
    {
        static void Main(string[] args)
        {
            int firstNum = Int32.Parse(Console.ReadLine());
            int secondNum = Int32.Parse(Console.ReadLine());

            for (int i = firstNum; i <= secondNum; i++)
                Console.Write($"{(char)i} ");
        }
    }
}
