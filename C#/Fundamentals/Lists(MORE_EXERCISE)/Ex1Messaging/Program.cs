using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex1Messaging
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] numbers = Console.ReadLine().Split().ToArray();
            List<char> text = Console.ReadLine().ToCharArray().ToList();
            string result = "";
            foreach (string num in numbers)
            {
                int numberSum = 0;
                foreach (char digit in num)
                    numberSum += int.Parse(digit.ToString());

                int index = 0;
                if (numberSum > text.Count())
                    index = numberSum % text.Count();
                else
                    index = numberSum;

                result += text[index];
                text.RemoveAt(index);
            }

            Console.WriteLine(result);
        }
    }
}
