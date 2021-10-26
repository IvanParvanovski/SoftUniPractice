using System;
using System.Collections.Generic;
using System.Linq;
using DefiningClasses;

namespace Ex4OpinionPoll
{
    public class StartUp
    {
        static void Main(string[] args)
        {
            List<Person> peopleOver30 = new List<Person>();
            int peopleCount = int.Parse(Console.ReadLine()!);

            for (int i = 0; i < peopleCount; i++)
            {
                string[] personData = Console.ReadLine()!.Split();
                int age = int.Parse(personData[1]);
                
                if (age > 30)
                {
                    peopleOver30.Add(new Person(personData[0], age));
                }
            }

            foreach (Person person in peopleOver30.OrderBy(p => p.Name))
            {
                Console.WriteLine($"{person.Name} - {person.Age}");
            }
        }
    }
}