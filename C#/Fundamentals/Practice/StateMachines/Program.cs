using System;

namespace StateMachines
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(ContainsNano("aBchNanoAwdaw"));
            Console.WriteLine(CountNano("abcNanoNanONaNoAbc"));
        }
        public static bool ContainsNano(string text)
        {
            string result = "";
            foreach (char symbol in text)
            {
                if (result == "nano")
                    return true;
                
                switch (Char.ToLower(symbol))
                {
                    case 'n':
                        result += 'n';
                        break;
                    case 'a':
                        if (result.Contains('n'))
                            result += 'a';
                        break;
                    case 'o':
                        if (result.Contains('n'))
                            result += 'o';
                        break;
                    default:
                        result = "";
                        break;
                }
            }
            return false;
        }
        
        public static int CountNano(string text)
        {
            string result = "";
            int count = 0;
            foreach (char symbol in text)
            {
                if (result == "nano")
                {
                    count++;
                    result = "";
                }
                
                switch (Char.ToLower(symbol))
                {
                    case 'n':
                        result += 'n';
                        break;
                    case 'a':
                        if (result.Contains('n'))
                            result += 'a';
                        break;
                    case 'o':
                        if (result.Contains('n'))
                            result += 'o';
                        break;
                    default:
                        result = "";
                        break;
                }
            }
            return count;
        }
    }
}