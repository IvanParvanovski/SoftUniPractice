using System;

namespace Ex7ProjectsCreation
{
class Program
{
    static void Main(string[] args)
    {
        string architect = Console.ReadLine();
        int projects = int.Parse(Console.ReadLine());
        
        Console.WriteLine($"The architect {architect} will need {3 * projects} hours to complete {projects} project/s.");
    }
}
}
