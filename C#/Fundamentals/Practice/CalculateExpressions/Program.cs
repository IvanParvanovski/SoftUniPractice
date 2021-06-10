using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace CalculateExpressions
{
    class Program
    {
        static void Main(string[] args)
        {
            // Console.WriteLine(Evaluate(Console.ReadLine()));
            Console.WriteLine(Evaluate2(Console.ReadLine()));
        }
        
        public static int Evaluate2(string expression)
        {
            Stack<char> operators = new Stack<char>();
            Stack<int> nums = new Stack<int>();
            Dictionary<char, Func<int, int, int>> operatorsDict = new Dictionary<char, Func<int, int, int>>
            {
                {'+', (a, b) => a + b },
                {'*', (a, b) => a * b },
                {'-', (a, b) => b - a },
            };
            
            foreach (char symbol in expression)
            {
                if (operatorsDict.ContainsKey(symbol))
                {
                    operators.Push(symbol);
                }
                else if (symbol >= '0' && symbol <= '9')
                {
                    nums.Push(symbol - '0');
                }
                else if (symbol == '(')
                {
                    nums.Push('(');
                }
                else if (symbol == ')')
                {
                    char operatorToCal = operators.Pop();
                    int result = operatorToCal == '*' ? 1 : 0;
                    
                    while (nums.Peek() != '(')
                    {
                        result = operatorsDict[operatorToCal](result, nums.Pop());
                    }
                    
                    nums.Pop();
                    nums.Push(result);
                }
            }
            return nums.Peek();
        }
        
        public static int Evaluate(string expression)
        {
            Stack<char> operators = new Stack<char>();
            Stack<int> nums = new Stack<int>();
            foreach (char symbol in expression)
            {
                if (symbol == '+' || symbol == '*')
                {
                    operators.Push(symbol);
                }
                else if (symbol >= '0' && symbol <= '9')
                {
                    nums.Push(symbol - '0');
                }
                else if (symbol == ')')
                {
                    int firstNum = nums.Pop();
                    int secondNum = nums.Pop();
                    char operatorToCal = operators.Pop();
                    int result = 0;
                    
                    if (operatorToCal == '*')
                    {
                        result = firstNum * secondNum;
                    }
                    else if (operatorToCal == '+')
                    {
                        result = firstNum + secondNum;
                    }
                    else if (operatorToCal == '-')
                    {
                        result = secondNum - firstNum;
                    }

                    nums.Push(result);
                }
            }
            return nums.Peek();
        }

    }
}