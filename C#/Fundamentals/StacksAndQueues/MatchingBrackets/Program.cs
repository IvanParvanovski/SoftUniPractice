using System;
using System.Collections.Generic;


namespace MatchingBrackets
{
    class Program
    {
        static void Main(string[] args)
        {
            string expression = Console.ReadLine();
            Stack<int> indexes = new Stack<int>();

            for (int i = 0; i < expression.Length; i++)
            {
                char currentSymbol = expression[i];
                if (currentSymbol == '(')
                {
                    indexes.Push(i);
                }
                else if (currentSymbol == ')')
                {
                    int startIndex = indexes.Pop();
                    Console.WriteLine(expression.Substring(startIndex, i - startIndex + 1));
                }
            }
        }
    }
}