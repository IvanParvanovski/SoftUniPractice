using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex6OrderByAge
{
    class Program
    {
        static void Main(string[] args)
        {
            List<Person> people = new List<Person>();
            while (true)
            {
                string input = Console.ReadLine();
                if (input == "End")
                    break;
                
                string[] data = input?.Split(' ', StringSplitOptions.RemoveEmptyEntries);
                string name = data?[0];
                string id = data?[1];
                int age = int.Parse(data?[2]!);

                Person person = new Person(name, id, age);
                people.Add(person);
            }
            
            foreach (Person person in people.OrderBy(x => x.Age))
                Console.WriteLine(person);
        }
    }
}