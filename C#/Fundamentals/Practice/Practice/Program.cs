using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Practice
{
    class Program
    {
        static void Main(string[] args)
        {
            int applesAmount = 0;
            
            CountApples(ref applesAmount);
            CountApples(ref applesAmount);
            CountApples(ref applesAmount);
            CountApples(ref applesAmount);
            CountApples(ref applesAmount);
            CountApples(ref applesAmount);
            CountApples(ref applesAmount);
            CountApples(ref applesAmount);

            Console.WriteLine("Outside: " + applesAmount);
        }
        private static void CountApples(ref int applesAmount)
        {
            applesAmount++;
            Console.WriteLine("Inside: " + applesAmount);
        }
   
    }
}
