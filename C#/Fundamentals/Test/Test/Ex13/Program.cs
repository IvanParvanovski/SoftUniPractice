using System;
using System.Collections.Generic;

namespace Ex13
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] data = Console.ReadLine()!.Split();
            Queue<char> firstString = new Queue<char>(data[0]);
            Queue<char> secondString = new Queue<char>(data[1]);
            double total = 0;

            Queue<char> startQueue;
            Queue<char> otherQueue;

            if (firstString.Count > secondString.Count)
            {
                startQueue = secondString;
                otherQueue = firstString;
            }
            else
            {
                startQueue = firstString;
                otherQueue = secondString;
            }

            while (startQueue.Count > 0)
            {
                char firstElement = startQueue.Dequeue();
                char secondElement = otherQueue.Dequeue();

                total += firstElement * secondElement;
            }

            while (otherQueue.Count > 0)
            {
                total += otherQueue.Dequeue();
            }

            Console.WriteLine(total);
        }
    }
}