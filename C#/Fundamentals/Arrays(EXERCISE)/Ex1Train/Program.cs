using System;
using System.Linq;

namespace Ex1Train
{
    class Program
    {
        static void Main(string[] args)
        {
            int wagons = int.Parse(Console.ReadLine());
            int[] peopleInTrain = new int[wagons];

            for (int i = 0; i < wagons; i++)
                peopleInTrain[i] = int.Parse(Console.ReadLine());

            int people = peopleInTrain.Sum();
            foreach (int peoplePerWagon in peopleInTrain)
                Console.Write(peoplePerWagon + " ");
            Console.WriteLine("\n" + people);
        }
    }
}
