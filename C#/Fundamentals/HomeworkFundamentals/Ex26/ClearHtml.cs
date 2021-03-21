using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace Ex26
{
    public class ClearHtml
    {
        public string Result { get; set; }
        private string Text { get; set; }
        private List<string> ImportantTags { get; set; }

        public ClearHtml(string text, List<string> importantTags)
        {
            this.ImportantTags = importantTags;
            this.Text = text;
            this.Result = ResultHtml(this.Text, this.ImportantTags);
        }

        public string ResultHtml(string text, List<string> importantTags)
        {
            // Clears the html
            // Removes tags, reduce the number of spaces, and add new lines
            
            string result = text;
            result = RemoveImportantTags(result, importantTags);
            result = RemoveOtherTags(result);
            result = ReduceSpaces(result);
            result = AddNewLines(result);
            
            return result;
        }

        private string RemoveImportantTags(string text, List<string> importantTags)
        {
            // Removes the tags such as: <body> or <title>
            
            string resultText = text;
            foreach (string importantTag in importantTags)
            {
                Regex regex = new Regex(importantTag);
                resultText = regex.Replace(resultText, match => $"{Capitalize(match.Groups["TagTitle"].Value)}: " + $"{match.Groups["TagData"].Value}");
            }

            return resultText;
        }

        private string RemoveOtherTags(string text)
        {
            // Removes tags such as: <a>, <head>, <html> ...
            
            Regex regex = new Regex(@">(?<tagData>.*?)<");
            MatchCollection resultInnerText = regex.Matches(text);
            string resultText = string.Join("", resultInnerText.Select(x => x.Groups["tagData"].Value));
            
            return resultText;
        }

        private string ReduceSpaces(string text)
        {
            // Reduce the number of spaces from MANY -> ONE
            
            Regex spaceRegex = new Regex(@"\s+");
            string resultText = spaceRegex.Replace(text, " ");
            
            return resultText.Trim();
        }

        private string AddNewLines(string text)
        {
            // Add new lines before important tags
            
            Regex newLineRegex = new Regex(@"\b(?<text>[A-Z][a-z]+:)");
            string resultText = newLineRegex.Replace(text, match => "\n" + match.Groups["text"].Value);
            
            return resultText;
        }
        
        private string Capitalize(string text)
        {
            // Makes the first letter of string upper
            
            return char.ToUpper(text[0]) + text.Substring(1, text.Length - 1);
        }

    }
}