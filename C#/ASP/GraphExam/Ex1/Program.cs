using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Linq;

namespace Ex1
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            int companiesCount = int.Parse(Console.ReadLine());
            Dictionary<string, string> companies = new Dictionary<string, string>();

            for (int i = 0; i < companiesCount; i++)
            {
                string[] companyData = Console.ReadLine().Split(" | ");
                string name = companyData[0];
                string owner = companyData[1];

                companies[owner] = name;
            }

            string[] range = Console.ReadLine().Split(" - ");

            char startChr = Convert.ToChar(range[0].ToLower());
            char endChr = Convert.ToChar(range[1].ToLower());

            foreach (var kvp in companies.OrderBy(x => x.Key))
            {
                char firstWordChar = kvp.Key.ToLower()[0];

                if (firstWordChar >= startChr && firstWordChar < endChr)
                {
                    Console.WriteLine($"{kvp.Key} - {kvp.Value}");
                }
            }
        }
    }
}