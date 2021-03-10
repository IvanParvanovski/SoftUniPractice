using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex3MergingLists
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> firstList = Console.ReadLine().Split().Select(int.Parse).ToList();
            List<int> secondList = Console.ReadLine().Split().Select(int.Parse).ToList();

            int indexToAdd = 1;
            for (int i = 0; i < firstList.Count; i++)
            {
                if (i >= secondList.Count || i < 0)
                    break;

                if (i + indexToAdd > firstList.Count)
                    indexToAdd--;

                firstList.Insert(i + indexToAdd, secondList[i]);
                indexToAdd++;
            }
            
            Console.WriteLine(string.Join(" ", firstList));
        }
    }
}
