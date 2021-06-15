using System;
using System.Collections.Generic;
using System.Linq;

namespace Ex6BalancedParenthesis
{
    class Program
    {
        static void Main(string[] args)
        {
            Queue<char> input = new Queue<char>(Console.ReadLine()!);
            
            Stack<char> parentheses = new Stack<char>();
            char[] openers = new[]
            {
                '(',
                '{',
                '[',
            };

            char[] closures = new[]
            {
                ')',
                '}',
                ']',
            };

            Dictionary<char, char> duals = new Dictionary<char, char>()
            {
                { '(', ')' },
                { '{', '}' },
                { '[', ']' },
            };

            bool valid = true;
            while (input.Count > 0 )
            {
                char currentBracket = input.Dequeue();

                if (openers.Contains(currentBracket))
                {
                    parentheses.Push(currentBracket);
                }
                else if (closures.Contains(currentBracket))
                {
                    if (parentheses.Count > 0)
                    {
                        char lastBracket = parentheses.Pop();
                        if (duals[lastBracket] != currentBracket)
                        {
                            valid = false;
                            break;
                        }
                    }
                    else
                    {
                        valid = false;
                        break;
                    }

                }
            }

            Console.WriteLine(valid ? "YES" : "NO");
        }
    }
}