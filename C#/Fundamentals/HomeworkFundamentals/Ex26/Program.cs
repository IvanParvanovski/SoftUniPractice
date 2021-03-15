using System;
using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using System.Text.RegularExpressions;

namespace Ex26
{
    class Program
    {
        static void Main(string[] args)
        {
            string text = Console.ReadLine();
            
            string titlePattern = @"<(?<TagTitle>title)>(?<TagData>.*)<\/title>";
            string bodyPattern = @"<(?<TagTitle>body)>(?<TagData>.*)<\/body>";
            List<string> importantTags = new List<string> {titlePattern, bodyPattern};

            string result = text;
            foreach (string importantTagPattern in importantTags)
            {
                Regex regex = new Regex(importantTagPattern);
                Match tagText = regex.Match(text);
   
                string tagTitle = tagText.Groups["TagTitle"].ToString();
                string tagData = tagText.Groups["TagData"].ToString();

                Regex tagRegex = new Regex(@">(.*?)<");
                MatchCollection insideInformation = tagRegex.Matches(tagData);
                string insideInformationResult = "";
                if (insideInformation.Count != 0)
                    insideInformationResult = string.Join("", insideInformation).Replace("<", "").Replace(">", "");
                else
                    insideInformationResult = tagData;
                
                Console.WriteLine($"{char.ToUpper(tagTitle[0]) + tagTitle.Substring(1, tagTitle.Length - 1)}: {insideInformationResult}");
            }
        }
    }
}