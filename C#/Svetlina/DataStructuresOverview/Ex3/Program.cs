using System;
using System.Collections.Generic;

namespace Ex3
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            int[] numbers = Array.ConvertAll(
                Console.ReadLine().Split(new string[] { ", " }, StringSplitOptions.None), x => int.Parse(x)
            );

            Console.WriteLine(SumOfUnique(numbers));
        }

        public static int SumOfUnique(int[] numbers)
        {
            int sum = 0;

            var props = new Dictionary<int, int>();
            foreach (int n in numbers)
            {
                if (!props.ContainsKey(n))
                {
                    props[n] = 0;
                }

                props[n]++;
            }

            foreach (KeyValuePair<int, int> entry in props)
            {
                if (entry.Value == 1)
                {
                    sum += entry.Key;
                }
            }

            return sum;
        }
    }
}
