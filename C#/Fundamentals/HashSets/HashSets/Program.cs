using System;
using System.Collections.Generic;

namespace HashSets
{
    class Program
    {
        static void Main(string[] args)
        {
            HashSet<string> mySet = new HashSet<string>();
            mySet.Add("C");
            mySet.Add("C");
            mySet.Add("B");
            mySet.Add("A");
            mySet.Add("B");
            mySet.Add("A");
            foreach (string symbol in mySet)
            {
                Console.WriteLine(symbol);
            }

            Console.WriteLine();
            
            SortedSet<string> sortedSet = new SortedSet<string>();
            sortedSet.Add("C");
            sortedSet.Add("C");
            sortedSet.Add("B");
            sortedSet.Add("A");
            sortedSet.Add("B");
            sortedSet.Add("A");
            foreach (string symbol in sortedSet)
            {
                Console.WriteLine(symbol);
            }
        }
    }
    
}
