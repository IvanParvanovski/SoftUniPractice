using System;
using System.Collections.Generic;

namespace HotPotato
{
    class Program
    {
        static void Main(string[] args)
        {
            Queue<string> children = new Queue<string>(Console.ReadLine()!.Split());
            int potatoNum = int.Parse(Console.ReadLine()!);
            while (children.Count != 1)
            {
                for (int i = 1; i < potatoNum; i++ )
                    children.Enqueue(children.Dequeue());
                Console.WriteLine($"Removed {children.Dequeue()}");
            }
            Console.WriteLine($"Last is {children.Dequeue()}");        }
    }
}