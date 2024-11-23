using System;

namespace Ex1Exam
{
    public class Program
    {
        public static void Main (string[] args)
        {
            var input = Console.ReadLine().ToArray();
            List<char> currentSequence = new List<char>();

            GenerateStrings(input, 0, currentSequence);
        }
        
        private static void GenerateStrings(
            char[] userInput,
            int i,
            List<char> currentSequence)
        {
            if (i == userInput.Length)
            {
                Console.WriteLine(string.Join("", currentSequence));
                return;
            }

            char currentChar = userInput[i];
            int newIndex = i + 1;

            if (!Char.IsLetter(currentChar))
            {
                currentSequence.Add(currentChar);
                GenerateStrings(userInput, newIndex, currentSequence);
            }
            else
            { 
                var currentSequenceUpper = currentSequence.ToList();
                currentSequenceUpper.Add(char.ToUpper(currentChar));
                GenerateStrings(userInput, newIndex, currentSequenceUpper);

                var currentSequenceLower = currentSequence.ToList();
                currentSequenceLower.Add(char.ToLower(currentChar));
                GenerateStrings(userInput, newIndex, currentSequenceLower);
            }
        }
    }
}
