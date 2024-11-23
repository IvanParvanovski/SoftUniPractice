using System.Text;

namespace MorseCode
{
    public class Program
    {
        public static void Main(string[] args)
        {
            var symbolArray = new List<string>
            {
                ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
            };

            var uniqueCombinations = new HashSet<string>();
            string[] words = new string[] {"gin", "zen", "gig", "msg"};

            foreach (string w in words)
            {
                StringBuilder sb = new StringBuilder();

                foreach (char symbol in w)
                {
                    sb.Append(symbolArray[symbol - 97]);
                }

                uniqueCombinations.Add(sb.ToString());
            }

            Console.WriteLine(uniqueCombinations.Count);
        }
    }
}