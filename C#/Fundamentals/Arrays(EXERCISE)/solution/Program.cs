using System;
using System.Collections;
using System.Linq;

namespace solution
{
    class Program
    {
        static void Main(string[] args)
        {
            int DNALength = int.Parse(Console.ReadLine());
            int index = 0;

            int[] bestDNA = new int[DNALength];
            int bestDNARepeatingElementsStartIndex = int.MaxValue;
            int bestDNAIndex = 0;

            while (true)
            {
                string userInput = Console.ReadLine();
                if (userInput == "Clone them!")
                    break;

                int[] dnaElements = userInput.Split('!').Select(int.Parse).ToArray();
                int currentDNAStartingIndex = GetDNARepeatingElementsIndex(dnaElements);
                index++;

                if (bestDNARepeatingElementsStartIndex > currentDNAStartingIndex)
                {
                    bestDNA = dnaElements;
                    bestDNARepeatingElementsStartIndex = currentDNAStartingIndex;
                    bestDNAIndex = index;
                }

                else if (bestDNARepeatingElementsStartIndex == currentDNAStartingIndex)
                {
                    if (bestDNA.Sum() < dnaElements.Sum())
                    {
                        bestDNA = dnaElements;
                        bestDNARepeatingElementsStartIndex = currentDNAStartingIndex;
                        bestDNAIndex = index;
                    }
                }

            }

            Console.WriteLine($"Best DNA sample {bestDNAIndex} with sum: {bestDNA.Sum()}." +
                              $"\n{string.Join(' ', bestDNA)}");
        }

        private static int GetDNARepeatingElementsIndex(int[] elements)
        {
            string longestSequence = "";
            int longestSequenceIndex = 0;
            string elementSequence = " ";
            int elementStartingIndex = 0;

            for (int i = 0; i < elements.Length; i++)
            {
                int element = elements[i];
                string elementFromSeq = Convert.ToString(elementSequence[0]);

                if (elementFromSeq != element.ToString())
                {
                    elementSequence = "";
                    elementStartingIndex = i;
                }

                elementSequence += $"{element} ";
                elementStartingIndex++;

                if (elementSequence.Length > longestSequence.Length)
                {
                    longestSequence = elementSequence;
                    longestSequenceIndex = elementStartingIndex;
                }
            }
            return longestSequenceIndex;
        }
    }
}
