using System;
using System.Linq;

namespace Ex5
{
    class Program
    {
        static void Main(string[] args)
        {
            // Input: 
            // We are living in a yellow submarine. We don't have anything else. Inside the submarine is very tight. So we are drinking all the day. We will move out of it in 5 days.
            // In
            
            // Read user's input.
            string text = Console.ReadLine();
            
            // Read the searched word, phrase, or sub text.
            string subText = Console.ReadLine();
            
            // Count the searched text in the user's input. 
            Console.WriteLine(CountWord(text, subText, -1, 0));
        }
        private static int CountWord(string text, 
                                     string subText, 
                                     int index,
                                     int counter)
        {
            // !!!
            // At the beginning the start index should be -1,
            // Because -1 + 1 = 0
            // -1 -> main index
            // +1 -> newIndex variable functionality
            // 0 should be start index, so that every substring is counted
            
            // Get the index of the substring in the text.
            // Increase it by 1, so it does not repeat.
            // Check if it is -1 and if it is, return the increased counter
            
            int newIndex = text.IndexOf(subText, index + 1, StringComparison.OrdinalIgnoreCase);
            
            if (newIndex == -1)
                return counter;
            
            return CountWord(text, subText, newIndex, ++counter);
        }
    }
}