using System;
using System.Collections.Generic;

namespace Ex5SoftUniParking
{
    class Program
    {
        static void Main(string[] args)
        {
            int usersQuantity = int.Parse(Console.ReadLine());
            Dictionary<string, string> peopleLicenses = new Dictionary<string, string>();

            for (int i = 0; i < usersQuantity; i++)
            {
                string[] userData = Console.ReadLine().Split();

                string command = userData[0];
                string person = userData[1];

                if (command == "register")
                {
                    string license = userData[2];

                    if (peopleLicenses.ContainsKey(person))
                    {
                        Console.WriteLine($"ERROR: already registered with plate number {peopleLicenses[person]}");
                        continue;
                    }

                    peopleLicenses[userData[1]] = license;
                    Console.WriteLine($"{person} registered {license} successfully");
                }

                else if (command == "unregister")
                {
                    if (!peopleLicenses.ContainsKey(person))
                    {
                        Console.WriteLine($"ERROR: user {person} not found");
                        continue;
                    }

                    peopleLicenses.Remove(person);
                    Console.WriteLine($"{person} unregistered successfully");
                }
            }

            foreach (var data in peopleLicenses)
                Console.WriteLine($"{data.Key} => {data.Value}");
        }
    }
}
