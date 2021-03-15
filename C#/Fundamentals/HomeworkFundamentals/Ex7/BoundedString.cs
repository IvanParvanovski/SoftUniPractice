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
            this.InputString = text;
            if (this.InputString.Length >= MaxLength)
                this.InputString = this.InputString.Substring(0, MaxLength);
            
            this.Result = AddStars(this.InputString);
        }

        private string AddStars(string text)
        {
            int neededStars = MaxLength - text.Length;
            return text + new String('*', neededStars);
        }

    }
}