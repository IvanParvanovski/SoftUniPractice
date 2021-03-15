using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex15
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, string> words = new Dictionary<string, string>();

            while (true)
            {
                string text = Console.ReadLine();
                if (text == "End")
                    break;
                string[] data = text.Split(" - ");
                words[data[0]] = data[1];
            }

            string searchedWord = Console.ReadLine();
            try
            {
                Console.WriteLine(words[searchedWord]);
            }
            catch (KeyNotFoundException)
            {
                Console.WriteLine($"The searched word ({searchedWord}) is missing!");
            }


        }
    }
}