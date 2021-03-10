using System;
using System.Collections.Generic;

namespace Ex2MinerTask
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, int> resources = new Dictionary<string, int>();
            
            while (true)
            {
                string input = Console.ReadLine();
                if (input == "stop") break;

                int quantity = int.Parse(Console.ReadLine());

                if (!resources.ContainsKey(input))
                    resources[input] = 0;
                resources[input] += quantity;
            }

            foreach (var result in resources)
                Console.WriteLine($"{result.Key} -> {result.Value}");
        }
    }
}
