using System;

namespace Ex3Elevator
{
    class Program
    {
        static void Main(string[] args)
        {
            int people = Int32.Parse(Console.ReadLine());
            int elevatorCapacity = Int32.Parse(Console.ReadLine());

            Console.WriteLine(CalculateCourses(people, elevatorCapacity));
        }
        private static int CalculateCourses(int people, int elevatorCapacity)
        {
            return (int)Math.Ceiling((double) people / elevatorCapacity);
        }
    }
}
