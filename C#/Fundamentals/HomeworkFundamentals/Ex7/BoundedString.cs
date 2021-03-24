using System;
using System.Text;

namespace Ex7
{
    public class BoundedString
    {
        private const int MaxLength = 20;
        private string InputString { get; set; }
        public string Result { get; set; }
        public BoundedString(string text)
        {
            // Get input string
            // If it is LESS than the max length -> add stars
            // If it is MORE than the max length -> cut
            
            this.InputString = text;
            
            if (this.InputString.Length >= MaxLength)
                this.Result = this.InputString.Substring(0, MaxLength);
            else
                this.Result = AddStars(this.InputString);
        }

        private string AddStars(string text)
        {
            // Get a string and calculate the (max length - the lenght of the input)
            // Generate a string with '*' with the difference and return it.
            
            int neededStars = MaxLength - text.Length;
            return text + new String('*', neededStars);
        }

    }
}