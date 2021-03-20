using System;
using System.Linq;

namespace Ex3
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input: 
            // ((a+b)/5-d) [Valid]
            // ((a+b)/5-d)( [Invalid]
            // )(a+b)) [Invalid]

            // Read expression.
            string expression = Console.ReadLine();

            // Check if the expression has valid put brackets.
            Console.WriteLine(IsCorrect(expression));
        }

        private static bool IsCorrect(string expression)
        {
            // We have a counter to track the brackets.
            
            // If it is more or less than zero
            // Which means there is a bracket without a partner
            // return: False
            
            // If it is zero
            // Which means there isn't a bracket without a partner)
            // return: True
            
            int counter = 0;

            foreach (char symbol in expression)
            {
                if (symbol == '(')
                    counter++;
                else if (symbol == ')')
                    counter--;
            }

            if (counter > 0 || counter < 0)
                return false;
            return true;
        }
    }
}