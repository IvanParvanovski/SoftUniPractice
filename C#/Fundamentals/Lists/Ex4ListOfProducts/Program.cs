using System;
using System.Collections.Generic;

namespace Ex4ListOfProducts
{
    class Program
    {
        static void Main(string[] args)
        {
            int num = int.Parse(Console.ReadLine());
            List<string> words = new List<string>(num);
            for (int i = 0; i < num; i++)
                words.Add(Console.ReadLine());

            words.Sort();
           
            for (int i = 0; i < words.Count; i++)
                Console.WriteLine($"{i + 1}.{words[i]}");
        }
    }
}
