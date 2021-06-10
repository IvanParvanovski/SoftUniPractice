using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex3FashionBoutique
{
    class Program
    {
        static void Main(string[] args)
        {
            Stack<int> box = new Stack<int>(Console.ReadLine()!
                .Split(' ')
                .Select(int.Parse)
            );
            
            int capacity = int.Parse(Console.ReadLine()!);
            
            int racks = 0;
            int sum = 0;
            
            while (box.Count > 0)
            {
                int currentSize = sum + box.Peek();

                if (currentSize < capacity)
                {
                    sum += box.Pop();
                }
                else if (currentSize == capacity)
                {
                    racks++;
                    box.Pop();
                    sum = 0;
                }
                else
                {
                    racks++;
                    sum = box.Pop();
                }
            }

            if (sum > 0)
            {
                racks++;
            }

            Console.WriteLine(racks);
        }
    }
}