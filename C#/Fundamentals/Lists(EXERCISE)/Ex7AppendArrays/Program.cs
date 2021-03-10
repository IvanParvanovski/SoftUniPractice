using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex7AppendArrays
{
    class Program
    {
        static void Main(string[] args)
        {
        //    List<List<string>> data = Console.ReadLine().Split("|")
        //                                                .Select(x => x.Split(new[] { " " }, StringSplitOptions.RemoveEmptyEntries)
        //                                                .ToList()).ToList();

            List<string> data = Console.ReadLine().Split("|").ToList();

            while (data.Contains(" "))
                data.Remove(" ");

            List<List<string>> newSequences = data.Select(x => x.Split(new[] { " " }, StringSplitOptions.RemoveEmptyEntries).ToList()).ToList();
            newSequences.Reverse();

            string result = "";
            foreach (List<string> sequence in newSequences)
                result = string.Join(" ", sequence) + " ";

            Console.WriteLine(result.Trim());

        }
    }
}
