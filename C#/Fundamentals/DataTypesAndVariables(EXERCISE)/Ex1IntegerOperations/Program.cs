using System;

namespace Ex1IntegerOperations
{
    class Program
    {
        static void Main(string[] args)
        {
            int firstNum = Int32.Parse(Console.ReadLine());
            int secondNum = Int32.Parse(Console.ReadLine());
            int thirdNum = Int32.Parse(Console.ReadLine());
            int forthNum = Int32.Parse(Console.ReadLine());

            Console.WriteLine((firstNum + secondNum) / thirdNum * forthNum);
        }
    }
}
