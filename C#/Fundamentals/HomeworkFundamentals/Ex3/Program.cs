using System;
using System.Linq;

namespace Ex3
{
    class Program
    {
        static void Main(string[] args)
        {
            string expression = Console.ReadLine();
           
            Console.WriteLine(IsCorrect(expression));
        }

        private static bool IsCorrect(string expression)
        {
            int counter = 0;

            foreach (char symbol in expression)
            {
                if (symbol == '(')
                    counter++;
                else if (symbol == ')')
                    counter--;

                if (counter < 0)
                    return false;
            }

            return true;
        }
    }
}