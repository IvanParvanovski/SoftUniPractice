using System;

namespace Ex6TriplesOfLationLetters
{
    class Program
    {
        static void Main(string[] args)
        {
            int num = Int32.Parse(Console.ReadLine());

            for (char i = 'a'; i < num + 97; i++)
                for (int j = 'a'; j < num + 97; j++)
                    for (int k = 'a'; k < num + 97; k++)
                        Console.WriteLine($"{(char)i}{(char)j}{(char)k}");
        }
    }
}
