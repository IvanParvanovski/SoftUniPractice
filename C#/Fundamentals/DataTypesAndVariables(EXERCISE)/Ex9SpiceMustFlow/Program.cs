using System;

namespace Ex9SpiceMustFlow
{
    class Program
    {
        static void Main(string[] args)
        {
            int yieldSource = int.Parse(Console.ReadLine());
            int workedDays = 0;
            int spiceExtracted = 0;
            while (true)
            {
                if (yieldSource < 100)
                {
                    ExtractSpice(ref spiceExtracted);
                    break;
                }

                spiceExtracted += yieldSource;
                yieldSource -= 10;
                workedDays += 1;
                ExtractSpice(ref spiceExtracted);
            }

            Console.WriteLine(workedDays);
            Console.WriteLine(spiceExtracted);
        }

        private static void ExtractSpice(ref int extractedSpice)
        {
            extractedSpice -= 26;
            IsExtractedSpiceLessThanZero(ref extractedSpice);
        }
        private static void IsExtractedSpiceLessThanZero(ref int extractedSpice)
        {
            if (extractedSpice < 0)
                extractedSpice = 0;
        }
    }
}
