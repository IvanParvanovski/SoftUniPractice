using System;
using System.Collections.Generic;
using System.Linq;

namespace SortByName
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] input = Console.ReadLine()!
                .Split(", ")
                .Select(int.Parse)
                .ToArray();

            Dictionary<char, string> dict = new Dictionary<char, string>()
            {
                {'0', "zero"},
                {'1', "one"},
                {'2', "two"},
                {'3', "three"},
                {'4', "four"},
                {'5', "five"},
                {'6', "six"},
                {'7', "seven"},
                {'8', "eight"},
                {'9', "nine"}
            };
            
            Dictionary<string, int> dict2 = new Dictionary<string, int>()
            {
                {"zero", 0},
                {"one", 1},
                {"two", 2},
                {"three", 3},
                {"four", 4},
                {"five", 5},
                {"six", 6},
                {"seven", 7},
                {"eight", 8},
                {"nine", 9}
            };

            List<string> result = new List<string>();
            for (int i = 0; i < input.Length; i++)
            {
                string currentNumber = input[i].ToString();
                string currentWord = "";
                
                foreach (var digit in currentNumber)
                {
                    currentWord += dict[digit] + "-";
                }
                
                currentWord = currentWord.Remove(currentWord.Length - 1);
                
                result.Add(currentWord);
            }
            
            result.Sort();

            for (int i = 0; i < result.Count; i++)
            {
                string[] currentWord = result[i].Split('-').ToArray();
                string currentNumber = "";
                
                for (int j = 0; j < currentWord.Length; j++)
                {
                    currentNumber += dict2[currentWord[j]];
                }
                
                input[i] = int.Parse(currentNumber);
            }
            
            Console.WriteLine(string.Join(", ", input));
        }
    }
}