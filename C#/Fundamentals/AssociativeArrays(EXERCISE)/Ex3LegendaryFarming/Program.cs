using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex3LegendaryFarming
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, Dictionary<string, int>> prodcts = new Dictionary<string, Dictionary<string, int>>(); 
            Dictionary<string, int> resources = new Dictionary<string, int>
            {
                { "shards", 0 }, 
                { "fragments", 0 }, 
                { "motes", 0 }, 
            };

            Dictionary<string, int> junk = new Dictionary<string, int>();

            Dictionary<string, string> legendaryItems = new Dictionary<string, string>
            {
                { "shards", "Shadowmourne"  }, 
                { "fragments", "Valanyr" }, 
                { "motes", "Dragonwrath"}, 
            };

            string type = "";
            while (true)
            {
                if (type.Length != 0) break;

                string[] data = Console.ReadLine().Split();
                for (int i = 0; i < data.Length - 1; i += 2)
                {
                    int quantity = int.Parse(data[i]);
                    string resource = data[i + 1].ToLower();

                    if (!resources.ContainsKey(resource))
                    {
                        if (!junk.ContainsKey(resource))
                            junk[resource] = 0;
                        junk[resource] += quantity;
                        continue;
                    }

                    resources[resource] += quantity;
                    if (resources[resource] >= 250)
                    {
                        type = resource;
                        resources[resource] -= 250;
                        break;
                    }
                }
            }

            Console.WriteLine($"{legendaryItems[type]} obtained!");

            PrintDictionary(junk.OrderByDescending(x => x.Value)
                                .ThenBy(x => x.Key));

            PrintDictionary(junk.OrderBy(x => x.Key));
            
        }

        private static void PrintDictionary (IEnumerable<KeyValuePair<string, int>> dict)
        {
            dict = dict.ToDictionary(x => x.Key, x => x.Value);
            foreach (var item in dict)
                Console.WriteLine($"{item.Key}: {item.Value}");
        } 
    }
}
