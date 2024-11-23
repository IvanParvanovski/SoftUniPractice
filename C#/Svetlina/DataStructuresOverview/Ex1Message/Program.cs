using System;
using System.Collections;
using System.Collections.Generic;

namespace Ex1Message
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            var letters = new Stack<char>();
            string rawWords = Console.ReadLine();

            foreach (char symbol in rawWords)
            {
                if (symbol == '*')
                {
                    letters.Pop();
                }
                else
                {
                    letters.Push(symbol);
                }
            }

            string str = "";

            while (letters.Count != 0)
            {
                str += letters.Pop();
            }

            Console.WriteLine(str);
        }
    }
}
