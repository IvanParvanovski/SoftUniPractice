using System;
using System.Collections.Generic;

namespace SimpleCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] input = Console.ReadLine()!.Split();
            Array.Reverse(input);
            Stack<string> expression = new Stack<string>(input);

            while (expression.Count > 2)
            {
                int firstNum = int.Parse(expression.Pop());
                string operatorExpr = expression.Pop();
                int secondNum = int.Parse(expression.Pop());

                int result = 0;
                switch (operatorExpr)
                {
                    case "+":
                        result = firstNum + secondNum;
                        break;
                    case "-":
                        result = firstNum - secondNum;
                        break;
                }
                expression.Push(result.ToString());
            }
            Console.WriteLine(string.Join("", expression));

        }
    }
}