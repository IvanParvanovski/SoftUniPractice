using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex2ChangeList
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = Console.ReadLine().Split().Select(int.Parse).ToList();
            while (true)
            {
                string user_input = Console.ReadLine();

                if (user_input == "end")
                    break;

                string[] user_data = user_input.Split();
                string command = user_data[0];
                int number = int.Parse(user_data[1]);

                if (command == "Delete")
                    while (numbers.Contains(number))
                        numbers.Remove(number);
                
                else if (command == "Insert")
                    numbers.Insert(int.Parse(user_data[2]), number);
            }

            Console.WriteLine(string.Join(" ", numbers));
        }
    }
}
