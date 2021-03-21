using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Ex23
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input:
            // This is red car, this?         is blue!          car. this,          is       green.       car.    

            // Output:
            // blue car car car green is is is red this this This
            // blue -> 1
            // car -> 3
            // green -> 1
            // is -> 3
            // red -> 1
            // this -> 3

            
            // Read user's input
            Regex regex = new Regex(@"\s+|,+(\s+)?|!+(\s+)?|\.+(\s+)?|\?+(\s+)?");
            string userInput = regex.Replace(Console.ReadLine()!, " ").Trim();
            string[] words = userInput.Split();
            
            // Sort the words
            string[] orderedWords = words!.OrderBy(x => x).ToArray();
            
            // Initialize a dictionary to keep the words count
            Dictionary<string, int> result = new Dictionary<string, int>();
            
            // Add or increase the count of word in the dictionary
            foreach (string word in orderedWords)
            {
                string loweredWord = word.ToLower();
                if (!result.ContainsKey(loweredWord))
                    result[loweredWord] = 0;
                result[loweredWord]++;
            }

            // Print the result
            Console.WriteLine(string.Join(" ", orderedWords));
            foreach (var pair in result)
                Console.WriteLine($"{pair.Key} -> {pair.Value}");
        }
    }
}