using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex3TakeSkipRope
{
    class Program
    {
        static void Main(string[] args)
        {
            List<char> text = Console.ReadLine().ToCharArray().ToList();
            List<int> numbersList = text.Where(x => Char.IsDigit(x)).Select(x => int.Parse(x.ToString())).ToList();
            List<int> takeList = numbersList.Where(x => x % 2 == 0).ToList();
            List<int> skipList = numbersList.Where(x => x % 2 != 0).ToList();

            List<char> message = text.Where(x => Char.IsLetter(x)).ToList();


            List<char> result = new List<char>();

            for (int i = 0; i < takeList.Count(); i++)
            {
                result = text.Take(takeList[i]).ToList();
                text.RemoveAt();
            }



        }
    }
}
