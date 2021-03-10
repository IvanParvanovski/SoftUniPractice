using System;
using System.Linq;
using System.Text;

namespace Practice
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(Reverse("Ivan"));
            Console.WriteLine(Capitals("Hello. [form] [me]"));
        }
        
        public static string Reverse(string currentString)
        {
            StringBuilder myStr = new StringBuilder(currentString.Length);
            for (int i = 0; i < currentString.Length; i++)
                myStr.Insert(0, currentString[i]);
            
            return myStr.ToString();
        }

        static string Capitals(string text)
        {
            StringBuilder cap = new StringBuilder(text.Length);
            bool isCapital = false;
            foreach (char symbol in text)
            {
                if (symbol == '[')
                    isCapital = true;
                
                else if (symbol == ']')
                    isCapital = false;
                
                else
                {
                    if (isCapital)
                        cap.Append(char.ToUpper(symbol));
                    else
                        cap.Append(symbol);
                }
            }
            return cap.ToString();
        }
    }
}
