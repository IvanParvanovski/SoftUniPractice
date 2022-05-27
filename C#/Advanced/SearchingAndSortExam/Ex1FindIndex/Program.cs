// See https://aka.ms/new-console-template for more information

using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex1FindIndex
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            List<string> names = Console.ReadLine()!.Split(", ").ToList();
            string searchedName = Console.ReadLine()!;
            
            names.Add(searchedName);
            
            BubbleSort(names);
            Console.WriteLine(LinearSearch(names, searchedName));
        }

        public static void BubbleSort(List<string> names)
        {
            for (int i = 0; i < names.Count; i++)
            {
                for (int j = 1; j < names.Count; j++)
                {
                    if (String.CompareOrdinal(names[j - 1], names[j]) > 0)
                    {
                        Swap(names, j - 1, j);
                    }
                }
            }
        }

        public static int LinearSearch(List<string> names, string searchedVal)
        {
            for (int i = 0; i < names.Count; i++)
            {
                if (names[i] == searchedVal)
                {
                    return i;
                }
            }

            return -1;
        }

        public static void Swap(List<string> names, int index1, int index2)
        {
            string name = names[index1];
            names[index1] = names[index2];
            names[index2] = name;
        }
    }
}