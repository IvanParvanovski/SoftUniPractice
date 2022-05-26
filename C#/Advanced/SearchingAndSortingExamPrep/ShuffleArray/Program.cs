// See https://aka.ms/new-console-template for more information

using System;

namespace ShuffleArray
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            Random rnd = new Random();
            int[] elements = {2, 3, 6, 7, 8};

            for (int i = 0; i < elements.Length; i++)
            {
                int next = rnd.Next(i, elements.Length);
                int oldElement = elements[i];
                elements[i] = elements[next];
                elements[next] = oldElement;
            }

            Console.WriteLine(string.Join(" ", elements));
        }
    }
}