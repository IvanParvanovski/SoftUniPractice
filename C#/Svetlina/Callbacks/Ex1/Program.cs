// See https://aka.ms/new-console-template for more information

using System;
using System.Linq;

namespace Ex1
{
    public class Program
    {
        private delegate void GraduatedDelegate(int[] numbers);

        public static void Main(string[] args)
        {
            GraduatedDelegate sort = sortEven;
            Func<string, int> parser = n => int.Parse(n);
            
            int[] numbers = Console.ReadLine()!
                .Split(new string[] {", "}, StringSplitOptions.RemoveEmptyEntries)
                .Select(parser)
                .ToArray();
            
            sort.Invoke(numbers);

        }
        private static void sortEven(int[] numbers)
        {
            int i = 0;
            int[] res = new int[numbers.Length];
            
            foreach (int n in numbers.OrderBy(x => x))
            {
                if (n % 2 == 0)
                {
                    res[i] = n;
                    i++;
                }
            }

            Console.WriteLine(String.Join(", ", res));
        }
    }    
}